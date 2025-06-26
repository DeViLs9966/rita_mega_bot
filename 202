import sys
from pathlib import Path

def find_latin1_encoding_errors(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"Файл не найден: {file_path}")
        return

    with file_path.open("r", encoding="utf-8", errors="replace") as f:
        for lineno, line in enumerate(f, start=1):
            try:
                line.encode('latin-1')
            except UnicodeEncodeError as e:
                print(f"Ошибка кодировки в строке {lineno}: {line.strip()}")
                print(f" -> Невозможно закодировать символы с позиции {e.start} до {e.end}")
                print(f"   Проблемные символы: {repr(line[e.start:e.end])}")
                print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python find_latin1_error_lines.py путь_к_файлу")
        sys.exit(1)

    find_latin1_encoding_errors(sys.argv[1])
