import sys
import re

if len(sys.argv) < 2:
    print("Использование: python3 fix_auto_fix_loop_conflict.py <путь_к_check_bot_diagnostics.py>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Найдём определения функций auto_fix_loop
pattern = r"(async def auto_fix_loop\s*[^)]*:)"
matches = list(re.finditer(pattern, content))

if len(matches) < 2:
    print("Вторая функция auto_fix_loop не найдена. Исправления не нужны.")
    sys.exit(0)

# Получим позиции второй функции
second_func_start = matches[1].start()
second_func_end = None

# Чтобы найти конец второй функции - найдём следующую функцию или конец файла
func_pattern = r"^async def\s+\w+\s*[^)]*:"
lines = content.splitlines()
line_num = 0
for i, line in enumerate(lines):
    if re.search(pattern, line):
        if line_num == 1:
            second_func_line = i
            break
        line_num += 1
else:
    print("Ошибка поиска второй функции auto_fix_loop.")
    sys.exit(1)

# Найдём где заканчивается тело второй функции (отступы)
def get_indent_level(line):
    return len(line) - len(line.lstrip(" "))

start_indent = get_indent_level(lines[second_func_line])
end_line = second_func_line + 1
for i in range(second_func_line + 1, len(lines)):
    indent = get_indent_level(lines[i])
    if indent <= start_indent and lines[i].strip() != "":
        end_line = i
        break
else:
    end_line = len(lines)

# Переименуем вторую функцию и все вызовы auto_fix_loop без аргументов в auto_fix_loop_simple
# В пределах строк second_func_line до end_line заменим определение функции
lines[second_func_line] = lines[second_func_line].replace("async def auto_fix_loop(", "async def auto_fix_loop_simple(")

# Заменяем все вызовы auto_fix_loop() без аргументов на auto_fix_loop_simple()
# Чтобы не сломать вызовы с параметрами, сделаем замену строго "auto_fix_loop()" => "auto_fix_loop_simple()"
for i in range(len(lines)):
    lines[i] = re.sub(r"\bauto_fix_loop", "auto_fix_loop_simple()", lines[i])

# Запишем обратно в файл
with open(file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Вторая функция auto_fix_loop переименована в auto_fix_loop_simple и вызовы исправлены.")
