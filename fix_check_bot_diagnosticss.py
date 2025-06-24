import os
import re
import sys
import traceback
import logging

# Твои реальные данные (подставь свои)
TELEGRAM_BOT_TOKEN = " "
GITHUB_TOKEN = " "
USER_TELEGRAM_ID =  

# Пути к твоим скриптам
CHECK_SCRIPT_PATH = os.path.expanduser("~/rita_mega_bot/check_bot_diagnostics.py")
BACKUP_PATH = CHECK_SCRIPT_PATH + ".backup"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("fixer.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def backup_script():
    if os.path.exists(CHECK_SCRIPT_PATH):
        logging.info("Создаём резервную копию скрипта...")
        with open(CHECK_SCRIPT_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        with open(BACKUP_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Резервная копия создана: {BACKUP_PATH}")
    else:
        logging.error(f"Файл не найден: {CHECK_SCRIPT_PATH}")
        sys.exit(1)

def fix_indentation(content):
    # Приводим все табы к 4 пробелам
    lines = content.splitlines()
    fixed_lines = []
    for line in lines:
        # Заменяем табы на 4 пробела
        fixed_line = line.replace('\t', '    ')
        fixed_lines.append(fixed_line)
    return "\n".join(fixed_lines)

def fix_import_errors(content):
    # Если встретится импорт в середине файла, пытаемся переместить в начало
    # Для упрощения: переместим все импорты в начало (только стандартные и telegram.ext)
    import_lines = []
    other_lines = []
    for line in content.splitlines():
        if re.match(r'^\s*(import|from)\s+', line):
            import_lines.append(line)
        else:
            other_lines.append(line)
    # Уникальные импорты без дубликатов
    import_lines = list(dict.fromkeys(import_lines))
    return "\n".join(import_lines + [""] + other_lines)

def fix_syntax_errors(content):
    # Автоматически вставим отсутствующие except или finally после try, если в конце кода try без блока
    # Это очень упрощённый фикс, может не решать все случаи, но устранит ошибку "expected except or finally"
    pattern = r"(try:\s*\n(?:[ \t]+.+\n)+)([ \t]*)(?!except|finally)"
    repl = r"\1\2except Exception as e:\n\2    print(f'Автофикс: обработка исключения: {e}')\n"
    fixed_content = re.sub(pattern, repl, content, flags=re.MULTILINE)
    return fixed_content

def run_syntax_check(code):
    try:
        compile(code, "<string>", "exec")
        return True, None
    except SyntaxError as e:
        return False, e

def fix_script():
    backup_script()
    with open(CHECK_SCRIPT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    logging.info("Фиксим отступы...")
    content = fix_indentation(content)

    logging.info("Фиксим расположение импортов...")
    content = fix_import_errors(content)

    logging.info("Проверяем и фиксируем синтаксис try/except...")
    content = fix_syntax_errors(content)

    valid, error = run_syntax_check(content)
    if valid:
        logging.info("Синтаксис проверен — ошибок не найдено.")
    else:
        logging.error(f"Синтаксис после исправлений всё ещё содержит ошибки: {error}")
        logging.error("Исправляйте вручную или предоставьте новые логи.")
        return False

    with open(CHECK_SCRIPT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    logging.info("Скрипт успешно отфиксирован и сохранён.")

    return True

def main():
    logging.info("=== Старт фиксатора ошибок для check_bot_diagnostics.py ===")
    success = fix_script()
    if success:
        logging.info("Фиксация завершена успешно.")
        logging.info("Запускайте скрипт снова и проверяйте логи.")
    else:
        logging.error("Фиксация завершилась с ошибками.")

if __name__ == "__main__":
    main()
