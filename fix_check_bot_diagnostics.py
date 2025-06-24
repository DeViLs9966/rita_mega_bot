import sys
import re

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed_lines = []
    inside_analyze_func = False
    analyze_func_fixed = False
    analyze_func_indent = ""
    auto_fix_loop_count = 0
    auto_fix_loop_start = None
    auto_fix_loop_end = None

    # Найдём функцию analyze_and_fix_script и исправим сигнатуру
    for i, line in enumerate(lines):
        # Исправляем сигнатуру analyze_and_fix_script, если нужно
        if re.match(r"async def analyze_and_fix_script\s*", line):
            if "logger" not in line:
                # Добавляем logger=None внутрь скобок
                line = line.rstrip("\n").rstrip("):") + ", logger=None):\n"
                analyze_func_fixed = True

        # Определяем, где начинается и заканчивается вторая функция auto_fix_loop (без параметров)
        if re.match(r"async def auto_fix_loop\s*\s*:", line):
            auto_fix_loop_count += 1
            if auto_fix_loop_count == 2:
                auto_fix_loop_start = i

        if auto_fix_loop_start is not None and auto_fix_loop_end is None:
            # Функция закончится на пустой строке или следующей функции
            # Найдем конец функции (строка, не начинающаяся с пробелов или def)
            if i > auto_fix_loop_start:
                if re.match(r"^\s*async def\s", line) or re.match(r"^\S", line):
                    auto_fix_loop_end = i
        fixed_lines.append(line)

    # Если нашли вторую auto_fix_loop, удалим её
    if auto_fix_loop_start is not None and auto_fix_loop_end is None:
        auto_fix_loop_end = len(lines)

    if auto_fix_loop_start is not None:
        # Удаляем строки второй auto_fix_loop
        del fixed_lines[auto_fix_loop_start:auto_fix_loop_end]

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(fixed_lines)

    print(f"[✔] Файл {filename} отредактирован:")
    print(f"    - analyze_and_fix_script: добавлен аргумент logger (если отсутствовал)")
    if auto_fix_loop_start is not None:
        print(f"    - удалена вторая функция auto_fix_loop (без параметров)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python3 fix_check_bot_diagnostics.py <путь_к_check_bot_diagnostics.py>")
        sys.exit(1)
    filename = sys.argv[1]
    fix_file(filename)
