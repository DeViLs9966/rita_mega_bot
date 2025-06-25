import sys
import re
from pathlib import Path

def fix_exists_calls_in_file(filename):
    backup_filename = filename + ".bak"
    # Сделаем резервную копию
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()
    with open(backup_filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"[INFO] Создан бэкап: {backup_filename}")

    # Найдем все вызовы вида: что-то.exists()
    # Попробуем убедиться, что это не Path.exists()
    # Схема: ищем вызовы .exists(), но если перед точкой переменная - строка,
    # то заменяем ее на Path(переменная).exists()

    # В этой упрощенной версии заменим все вызовы вида: <переменная>.exists()
    # где <переменная> — возможно строка (имя переменной), на: Path(<переменная>).exists()

    # Регулярка для вызова: слово .exists()
    pattern = re.compile(r"(\b\w+)\.exists")

    def replacement(match):
        var = match.group(1)
        # Проверим, что var — не Path, не pathlib.Path, не pathlib.Path(). 
        # Для простоты будем считать, что если var уже обернут в Path, то не заменяем.
        # Тут заменим все, кроме случаев где var — "Path" или "pathlib" или уже Path(...)
        # Т.к. это сложно проверить в статике, заменим везде и потом попробуем избежать дублирования.
        # Чтобы не превращать Path(x).exists() в Path(Path(x)).exists(), проверим следующий код:
        return f"Path({var}).exists()"

    # Если в коде уже есть import Path, пропускаем вставку импорта
    if "from pathlib import Path" not in code:
        code = "from pathlib import Path\n" + code

    # Заменяем вызовы .exists()
    new_code = pattern.sub(replacement, code)

    # Уберем случаи двойного вызова: Path(Path(...)).exists()
    new_code = re.sub(r"PathPath(.*?)", r"Path(\1)", new_code)

    # Записываем обратно
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_code)

    print(f"[INFO] Файл {filename} пропатчен и сохранён.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python fix_exists_calls.py <имя_файла1> [<имя_файла2> ...]")
        sys.exit(1)
    for filename in sys.argv[1:]:
        if Path(filename).exists():
            fix_exists_calls_in_file(filename)
        else:
            print(f"[ERROR] Файл не найден: {filename}")
