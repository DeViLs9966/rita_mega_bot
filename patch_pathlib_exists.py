import sys
from pathlib import Path
import re

def patch_exists_calls(filenames):
    for filename in filenames:
        path = Path(filename)
        backup_path = path.with_suffix(path.suffix + ".bak")
        print(f"[INFO] Создан бэкап: {backup_path}")
        path.rename(backup_path)

        content = backup_path.read_text(encoding="utf-8")
        lines = content.splitlines()

        # Словарь переменных, которым присваивают строку пути
        path_vars = set()

        # Ищем переменные, которым присваивают строки (потенциально путь)
        assign_path_re = re.compile(r"^\s*(\w+)\s*=\s*['\"]([^'\"]+)['\"]\s*$")

        # Найдём строки, где вызывается .exists()
        exists_call_re = re.compile(r"(\w+)\.exists")

        new_lines = []
        for line in lines:
            m_assign = assign_path_re.match(line)
            if m_assign:
                var, val = m_assign.groups()
                # Пометим, что переменная assigned строка — кандидат на Path обертку
                path_vars.add(var)

            new_lines.append(line)

        # Второй проход — заменим объявление строковых путей на pathlib.Path
        fixed_lines = []
        for line in new_lines:
            m_assign = assign_path_re.match(line)
            if m_assign:
                var, val = m_assign.groups()
                if var in path_vars:
                    # Заменим присвоение строки на Path("...")
                    fixed_line = f"{var} = Path(\"{val}\")"
                    fixed_lines.append(fixed_line)
                    continue
            fixed_lines.append(line)

        # Третий проход — проверим .exists(), если у переменной нет обертки Path, добавим предупреждение
        # Но лучше этого не делать, т.к. не всегда можно понять статически.
        # Оставим так.

        # Добавим импорт pathlib.Path, если его нет
        text = "\n".join(fixed_lines)
        if "from pathlib import Path" not in text:
            text = "from pathlib import Path\n" + text

        path.write_text(text, encoding="utf-8")
        print(f"[INFO] Файл {filename} пропатчен и сохранён.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python3 patch_pathlib_exists.py <файл1> [файл2 ...]")
        sys.exit(1)
    patch_exists_calls(sys.argv[1:])
