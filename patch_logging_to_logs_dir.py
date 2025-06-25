import os
import re
from pathlib import Path

TARGET_FILES = ["rita_main.py", "check_bot_diagnostics.py"]
LOG_DIR = Path("logs")
LOG_FILENAME = "rita_bot.log"

# Создаём папку logs/, если нет
LOG_DIR.mkdir(parents=True, exist_ok=True)

def patch_log_paths(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        original = f.read()

    updated = original

    # Заменить пути к логам, если они явно указаны
    updated = re.sub(r'filename\s*=\s*["\'](.*?)\.log["\']',
                     f'filename="{LOG_DIR / LOG_FILENAME}"', updated)

    # Заменить LOG_FILE = Path("что-то.log")
    updated = re.sub(r'LOG_FILE\s*=\s*Path["\'](.*?)\.log["\']',
                     f'LOG_FILE = Path("{LOG_DIR / LOG_FILENAME}")', updated)

    # Только если были изменения
    if updated != original:
        # Сделать бэкап
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(original)

        # Сохранить обновлённый файл
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated)

        print(f"[✅] {file_path.name} обновлён. Бэкап: {backup_path.name}")
    else:
        print(f"[ℹ️] {file_path.name} не требует изменений.")

def main():
    print("[🔧] Обновляем пути логов на logs/rita_bot.log...")
    for filename in TARGET_FILES:
        path = Path(filename)
        if path.exists():
            patch_log_paths(path)
        else:
            print(f"[⚠️] Файл не найден: {filename}")

if __name__ == "__main__":
    main()
