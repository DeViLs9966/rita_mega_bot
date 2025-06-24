import sys
import re

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Найти все определения async def auto_fix_loop(...)
pattern = re.compile(r'async def auto_fix_loop.*?:')

matches = list(pattern.finditer(content))

if len(matches) < 2:
    print("Вторая функция auto_fix_loop не найдена. Исправления не нужны.")
    sys.exit(0)

second_start = matches[1].start()

# Найти позицию следующей функции после второй auto_fix_loop
next_func_pos = content.find('\nasync def ', second_start + 1)

if next_func_pos == -1:
    # Удаляем со второй функции до конца файла
    new_content = content[:second_start]
else:
    # Удаляем со второй функции до начала следующей функции
    new_content = content[:second_start] + content[next_func_pos:]

with open(filename, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Вторая функция auto_fix_loop удалена из {filename}.")
