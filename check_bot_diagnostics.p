
# check_bot_diagnostics.py — БЛОК 1 из 6
import datetime
import aiohttp
from pathlib import Path
import asyncio
import openai
import logging
import requests
import difflib
import datetime
import os
import sys
import time
import json
import logging
import asyncio
import subprocess
import importlib
import shutil
import requests
import traceback
import hashlib
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from pathlib import Path
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackContext
)
import os
import logging
import requests
from pathlib import Path
import hashlib
from telegram import Bot
import threading
import asyncio
import psutil
import time

import psutil
import sys

import psutil
import sys

import psutil
import sys

import os
import sys
import psutil
from telegram.error import Conflict
import os
os.environ['TZ'] = 'UTC'  # Устанавливаем переменную окружения TZ в UTC

import pytz  # Импортируем pytz, чтобы APScheduler не ругался на таймзону

import logging

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def read_logs():
    try:
        with open("rita_bot.log", "r", encoding="utf-8") as f:
            logs = f.read()
        logger.info("Логи успешно прочитаны.")
        return logs
    except FileNotFoundError:
        logger.error("Файл rita_bot.log не найден.")
        return ""

def is_another_check_diag_running():
    count = 0
    for proc in psutil.process_iter(['cmdline']):
        try:
            cmd = proc.info['cmdline']
            if cmd and 'check_bot_diagnostics.py' in ' '.join(cmd):
                count += 1
        except:
            pass
    return count > 1

def is_another_instance_running(script_name):
    count = 0
    for proc in psutil.process_iter(['cmdline']):
        try:
            cmd = proc.info['cmdline']
            if cmd and script_name in ' '.join(cmd):
                count += 1
        except Exception:
            pass
    return count > 1

# Проверка дубликата текущего скрипта
# Проверка дубликата текущего скрипта
if is_another_check_diag_running():
    logger.info("[INFO] Другой экземпляр check_bot_diagnostics.py уже запущен. Выход.")
    sys.exit(0)

# (Опционально) Проверка на дубликат rita_main.py
if is_another_instance_running("rita_main.py"):
    logger.info ("[INFO] Другой экземпляр rita_main.py уже запущен. Выход.")
    sys.exit(0)

        # Найдём начало блока запуска
import re

def fix_asyncio_run_block(filepath="rita_main.py"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        fixed_block = '''
if __name__ == "__main__":
    import asyncio
    import nest_asyncio

    nest_asyncio.apply()

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info ("[❌] Завершение работы по Ctrl+C или команде завершения.")
    except RuntimeError as e:
        if "Cannot close a running event loop" in str(e):
            logger.info ("[⚠️] Event loop уже запущен. Работа продолжается.")
        else:
            raise
'''
        # Проверяем, есть ли блок запуска
        if 'if __name__ == "__main__"' not in content:
            logger.info (f"[WARN] Блок запуска не найден в {filepath}, ничего не изменено.")
            return

        # Заменяем весь блок запуска на fixed_block
        content = re.sub(
            r'if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:\s*.*',
            fixed_block.strip(),
            content,
            flags=re.DOTALL
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        logger.info (f"[INFO] Блок запуска в {filepath} успешно обновлён.")

    except Exception as e:
          logger.info (f"[ERROR] Ошибка при исправлении {filepath}: {e}")

import os
import psutil
import subprocess
import time

def log_info(msg):
    # Твоя реализация логирования info, если есть
    print(f"[INFO] {msg}")

def log_error(msg):
    # Твоя реализация логирования ошибок, если есть
    print(f"[ERROR] {msg}")

def kill_existing_rita_bot():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and "rita_main.py" in " ".join(proc.info['cmdline']) and proc.pid != os.getpid():
                log_info(f"Завершаю дубликат процесса {proc.pid} (rita_main.py)")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def safe_restart_rita_main():
    kill_existing_rita_bot()
    time.sleep(2)
    try:
        proc = subprocess.Popen(["python3", "rita_main.py"])
        log_info(f"rita_main.py запущен с PID {proc.pid}")
    except Exception as e:
        log_error(f"Ошибка запуска rita_main.py: {e}")

import asyncio
from pathlib import Path

LOG_FILE_PATH = Path("check_bot_diagnostics.log")
MAIN_SCRIPT_PATH = Path("rita_main.py")
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")


from pathlib import Path

async def auto_fix_from_logs():
    log_info("[INFO] Запуск автоанализа логов...")

    try:
        # Обязательно оборачиваем в Path, чтобы избежать ошибок 'str' object has no attribute 'exists'
        rita_main_path = Path("rita_main.py")
        rita_log_path = Path("rita_main.log")

        check_bot_path = Path("check_bot_diagnostics.py")
        check_log_path = Path("check_logs.txt")

        # Отладочный вывод типов — чтобы убедиться, что всё обернуто правильно
        print(f"[DEBUG] rita_main_path = {type(rita_main_path)}, check_bot_path = {type(check_bot_path)}")

        await analyze_and_fix_script(Path(check_bot_path), Path(log_path))
        await analyze_and_fix_script(Path(rita_main_path), Path(log_path))
    except Exception as e:
        logger.error(f"[ERROR] auto_fix_from_logs: {e}")

async def main():
    try:
        await analyze_and_fix_script(Path(rita_main_path), Path(log_path))
    except Exception as e:
        logger.error(f"[ERROR] analyze_and_fix_script: {e}")

async def openai_fix_code(prompt: str) -> str:
    openai.api_key = OPENAI_API_KEY
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты — помощник программиста."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=2000,
            n=1,
        )
        fixed_code = response.choices[0].message.content.strip()
        return fixed_code
    except Exception as e:
        logger.error(f"[ERROR] OpenAI request failed: {e}")
        return ""

import requests

def send_telegram_notification(message: str):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": ADMIN_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        resp = requests.post(url, data=data, timeout=10)
        if not resp.ok:
            logger.error(f"[ERROR] Telegram notification failed: {resp.text}")
    except Exception as e:
        logger.error(f"[ERROR] Telegram notification exception: {e}")

from pathlib import Path

async def analyze_and_fix_script(script_path: Path, log_path: Path) -> bool:
    script_path = Path(script_path)
    log_path = Path(log_path)

    try:
        if not log_path.exists() or not script_path.exists():
            logger.info(f"Файл лога или скрипта не найден: {log_path}, {script_path}")
            return False

        log_content = log_path.read_text(encoding="utf-8")

        if "ERROR" not in log_content and "Traceback" not in log_content:
            logger.info(f"Ошибок в логе {log_path.name} не обнаружено.")
            return False

        script_content = script_path.read_text(encoding="utf-8")

        # Проверка на неправильный вызов asyncio.run(main)
        if "asyncio.run(main())" in script_content:
            safe_main_call = (
                "import asyncio\n\n"
                "if __name__ == '__main__':\n"
                "    try:\n"
                "        asyncio.run(main())\n"
                "    except (KeyboardInterrupt, SystemExit):\n"
                "        pass\n"
            )

            # Удаляем старую строку и добавляем безопасный вызов
            lines = script_content.splitlines()
            new_lines = [line for line in lines if "asyncio.run(main())" not in line]
            new_lines.append(safe_main_call)

            script_path.write_text("\n".join(new_lines), encoding="utf-8")
            logger.info(f"[INFO] ✅ {script_path.name}: исправлен вызов asyncio.run(main()) на безопасный")
            return True

        logger.info(f"[INFO] Не найдены известные ошибки для автоисправления в {script_path.name}")
        return False

    except Exception as e:
        logger.error(f"[ERROR] analyze_and_fix_script: {e}")
        return False

        # Пример автофикса — вставка asyncio.run(main()) если отсутствует
        script_code = script_path.read_text(encoding="utf-8")
        if "asyncio.run(main())" not in script_code:
            script_code += "\n\nif __name__ == '__main__':\n    asyncio.run(main())\n"
            script_path.write_text(script_code, encoding="utf-8")
            logger.info(f"[FIX] Добавлен вызов asyncio.run(main()) в {script_path.name}")
            return True

        logger.info(f"[INFO] Никаких автоисправлений не выполнено для {script_path.name}")
        return False

    except Exception as e:
        logger.error(f"[ERROR] Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False

        log_content = log_path.read_text(encoding="utf-8")
        if "ERROR" not in log_content and "Traceback" not in log_content:
            logger.info(f"Ошибок в логе {log_path.name} не обнаружено.")
            return False

        old_code = script_path.read_text(encoding="utf-8")

        prompt = (
            f"В логах ошибки:\n{log_content}\n\n"
            f"Вот текущий код:\n{old_code}\n\n"
            "Исправь ошибки и верни полный исправленный код."
        )

        new_code = await openai_fix_code(prompt)
        if not new_code:
            logger.error(f"Не удалось получить исправленный код для {script_path.name}")
            return False

        if new_code.strip() == old_code.strip():
            logger.info(f"Код в {script_path.name} не изменился после анализа.")
            return False

        diff = difflib.unified_diff(
            old_code.splitlines(keepends=True),
            new_code.splitlines(keepends=True),
            fromfile=f"{script_path.name} (old)",
            tofile=f"{script_path.name} (new)",
            lineterm=""
        )
        diff_text = "".join(diff)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        diff_log_path = script_path.parent / f"fix_diff_{script_path.stem}_{timestamp}.diff"
        diff_log_path.write_text(diff_text, encoding="utf-8")
        logger.info(f"Diff изменений сохранён в {diff_log_path}")

        script_path.write_text(new_code, encoding="utf-8")
        logger.info(f"✅ Исправление вставлено в {script_path.name}")

        # Отправка уведомления в Telegram
        send_telegram_notification(f"✅ В скрипт {script_path.name} внесены исправления. Подробнее: {diff_log_path.name}")

        return True

    except Exception as e:
        logger.error(f"[ERROR] Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False

    except Exception as e:
        logger.error(f"[ERROR] Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False


async def auto_fix_from_logs():
    fixed_main = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
    fixed_helper = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)

    if fixed_main or fixed_helper:
        log_info("Автоисправления применены при запуске.")

async def auto_fix_loop(interval_minutes: int = 5):
    while True:
        log_info("⏳ [Автофиксер] Запуск автоанализа и исправления скриптов...")
        try:
            main_updated = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
            helper_updated = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)

            if main_updated:
                await send_admin_message("✅ Основной скрипт auto-исправлен из логов!")

            if helper_updated:
                await send_admin_message("✅ Вспомогательный скрипт auto-исправлен из логов!")

        except Exception as e:
            log_error(f"Ошибка в auto_fix_loop: {e}")

        await asyncio.sleep(interval_minutes * 60)


async def auto_fix_loop():
    while True:
        await asyncio.sleep(300)  # 5 минут

        fixed_main = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
        fixed_helper = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)

        if fixed_main or fixed_helper:
            log_info("Автоисправления применены в фоне.")


import re

import re
import asyncio

# Парсим логи и собираем ошибки
def parse_error_logs(log_text):
    errors = []
    for line in log_text.splitlines():
        if "ERROR" in line or "Exception" in line:
            errors.append(line)
    return errors

async def generate_improvements(script_code: str, script_name: str) -> str:
    prompt = (
        f"Ты опытный Python-разработчик и улучшатель кода.\n"
        f"Это код файла {script_name}.\n"
        f"Добавь полезные улучшения, команды, автоанализ, оптимизацию, безопасность. "
        f"Не удаляй существующий функционал.\n"
        f"Верни только обновлённый ПОЛНЫЙ код без пояснений.\n\n"
        f"{script_code}"
    )
    try:
        openai.api_key = OPENAI_API_KEY
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=3500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        log_error(f"❌ GPT улучшение ошибки: {e}")
        return ""

import asyncio
from pathlib import Path

# Интервал проверки (в секундах)
AUTO_FIX_INTERVAL = 300  # 5 минут

async def generate_fix_patch(error_log_snippet: str, file_content: str) -> str:
    """
    Отправляет запрос в OpenAI для генерации исправленного кода на основе лога ошибок и текущего кода.
    Возвращает исправленный полный код.
    """
    prompt = (
        "В этом фрагменте лога ошибок:\n"
        f"{error_log_snippet}\n"
        "Предложи исправления для следующего кода:\n"
        f"{file_content}\n"
        "Верни исправленный полный код без объяснений."
    )
    try:
        openai.api_key = OPENAI_API_KEY
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=1500,
        )
        fixed_code = response.choices[0].message.content.strip()
        return fixed_code
    except Exception as e:
        log_error(f"Ошибка вызова OpenAI для исправления кода: {e}")
        return ""

import asyncio
from pathlib import Path
import sys
import subprocess
import time

# Пути к скриптам и логу (замени на свои пути, если надо)
MAIN_SCRIPT_PATH = Path("rita_main.py")
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
LOG_FILE_PATH = Path("check_bot_diagnostics.log")

# Глобальные переменные для хранения последних хешей файлов
last_main_hash = ""
last_helper_hash = ""

async def auto_fix_and_restart_loop():
    global last_main_hash, last_helper_hash

    while True:
        await asyncio.sleep(300)  # 300 секунд = 5 минут

        # Вычисляем текущие хеши
        current_main_hash = calculate_hash(MAIN_SCRIPT_PATH)
        current_helper_hash = calculate_hash(HELPER_SCRIPT_PATH)

        # Анализируем и исправляем rita_main.py при изменениях или ошибках
        if current_main_hash != last_main_hash:
            last_main_hash = current_main_hash
            log_info("Обнаружено изменение rita_main.py — анализируем и при необходимости исправляем")
            fixed = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
            if fixed:
                log_info("rita_main.py исправлен автоматически, перезапуск...")
                safe_restart_rita_main()

        # Анализируем и исправляем check_bot_diagnostics.py при изменениях или ошибках
        if current_helper_hash != last_helper_hash:
            last_helper_hash = current_helper_hash
            log_info("Обнаружено изменение check_bot_diagnostics.py — анализируем и при необходимости исправляем")
            fixed = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)
            if fixed:
                log_info("check_bot_diagnostics.py исправлен автоматически")


async def analyze_and_fix_script(script_path: Path, log_path: Path) -> bool:
    """
    Анализирует последние ошибки из лога и пытается исправить скрипт,
    перезаписывая файл, если OpenAI предлагает изменения.
    Возвращает True, если код был обновлен, иначе False.
    """
import subprocess
import sys
import psutil  # убедись, что psutil импортирован в начале файла

def kill_processes_by_script_name(script_name: str):
    """
    Завершает все процессы python, в которых в командной строке есть script_name.
    """
    try:
        for proc in psutil.process_iter(['pid', 'cmdline']):
            if proc.info['cmdline'] and script_name in " ".join(proc.info['cmdline']):
                log_info(f"Завершаем процесс PID {proc.pid} для {script_name}")
                proc.terminate()
                proc.wait(timeout=5)
    except Exception as e:
        log_error(f"Ошибка при завершении процессов {script_name}: {e}")

async def analyze_and_fix_script(script_path: Path, log_path: Path) -> bool:
    """
    Расширяем функцию — после обновления запускаем новый процесс и завершаем старый.
    """
    try:
        if not log_path.exists() or not script_path.exists():
            log_info(f"Файл лога или скрипта не найден: {log_path}, {script_path}")
            return False

        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        error_lines = [line for line in lines if "[ERROR]" in line]
        last_errors = "".join(error_lines[-100:]) if error_lines else ""

        if not last_errors:
            log_info(f"Ошибок для анализа не найдено в {script_path.name}, пропускаем исправление")
            return False

        current_code = script_path.read_text(encoding="utf-8")
        fixed_code = await generate_fix_patch(last_errors, current_code)

        if fixed_code and fixed_code != current_code:
            backup_path = script_path.with_suffix(script_path.suffix + ".bak")
            script_path.replace(backup_path)
            log_info(f"Создана резервная копия: {backup_path}")

            script_path.write_text(fixed_code, encoding="utf-8")
            log_info(f"✅ Автоматически применены исправления для {script_path.name}")

            # Запускаем новый процесс для обновленного скрипта
            try:
                subprocess.Popen([sys.executable, str(script_path.resolve())])
                log_info(f"Запущен новый процесс для {script_path.name}")
            except Exception as e:
                log_error(f"Ошибка запуска нового процесса для {script_path.name}: {e}")

            # Завершаем старый процесс (этот), если это вспомогательный скрипт
            # или завершаем процессы основного скрипта, если обновлен основной
            if script_path.name == "rita_main.py":
                kill_processes_by_script_name("rita_main.py")
            elif script_path.name == "check_bot_diagnostics.py":
                kill_processes_by_script_name("check_bot_diagnostics.py")

            return True
        else:
            log_info(f"⚠️ Исправления не были предложены или совпадают с текущим кодом для {script_path.name}")
            return False

    except Exception as e:
        log_error(f"❌ Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False
        # Читаем последние 200 строк логов и фильтруем ошибки
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        error_lines = [line for line in lines if "[ERROR]" in line]
        last_errors = "".join(error_lines[-100:]) if error_lines else ""

        if not last_errors:
            log_info(f"Ошибок для анализа не найдено в {script_path.name}, пропускаем исправление")
            return False

        # Читаем текущий код скрипта
        current_code = script_path.read_text(encoding="utf-8")

        # Запрашиваем исправления у OpenAI
        fixed_code = await generate_fix_patch(last_errors, current_code)

        if fixed_code and fixed_code != current_code:
            # Создаем резервную копию
            backup_path = script_path.with_suffix(script_path.suffix + ".bak")
            script_path.replace(backup_path)
            log_info(f"Создана резервная копия: {backup_path}")

            # Записываем исправленный код
            script_path.write_text(fixed_code, encoding="utf-8")
            log_info(f"✅ Автоматически применены исправления для {script_path.name}")
            return True
        else:
            log_info(f"⚠️ Исправления не были предложены или совпадают с текущим кодом для {script_path.name}")
            return False

    except Exception as e:
        log_error(f"❌ Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False

async def auto_fix_loop():
    """
    Основной цикл автоисправления обоих скриптов с интервалом AUTO_FIX_INTERVAL.
    """
    global MAIN_SCRIPT_PATH, HELPER_SCRIPT_PATH, LOG_FILE

    while True:
        try:
            updated_main = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
            updated_helper = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)

            if updated_main:
                log_info("Основной скрипт обновлен автоматически.")

            if updated_helper:
                log_info("Вспомогательный скрипт обновлен автоматически.")

        except Exception as e:
            log_error(f"Ошибка в auto_fix_loop: {e}")

        await asyncio.sleep(AUTO_FIX_INTERVAL)


# Генерируем список исправлений по ошибкам
def generate_fixes_for_errors(errors):
    fixes = []
    for err in errors:
        if "asyncio.run(main())" in err:
            fixes.append("fix_asyncio_run_block")
        if "Conflict: terminated by other getUpdates request" in err:
            fixes.append("kill_existing_rita_bot")
        # Добавь свои правила, если надо
    return fixes

# Применяем исправления
def apply_fixes(fixes):
    for fix in fixes:
        if fix == "fix_asyncio_run_block":
            logger.info ("[AUTO_FIX] Применяется исправление: безопасный вызов asyncio.run(main())")
            fix_asyncio_run_block()
        elif fix == "kill_existing_rita_bot":
            logger.info ("[AUTO_FIX] Применяется исправление: завершение дубликатов rita_main.py")
            kill_existing_rita_bot()

def remove_loop_close_from_rita():
    try:
        with open("rita_main.py", "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Удаляем строки, содержащие loop.close() в любом виде
        pattern = re.compile(r"\s*loop\s*\.\s*close\s*\s*\s*")
        new_lines = [line for line in lines if not pattern.fullmatch(line.strip())]

        if len(lines) != len(new_lines):
            with open("rita_main.py", "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            logger.info("[INFO] 🧼 Расширенно: loop.close() удалён")
        else:
            logger.info("[INFO] 🧼 loop.close() не найден (даже в скрытом виде)")
    except Exception as e:
        logger.info(f"[ERROR] ❌ Ошибка при удалении loop.close(): {e}")

def fix_rita_main_asyncio_run():
    try:
        with open("rita_main.py", "r", encoding="utf-8") as f:
            lines = f.readlines()

        changed = False
        new_lines = []
        for i, line in enumerate(lines):
            if "asyncio.run(main())" in line:
                new_lines.append("    loop = asyncio.get_event_loop()\n")
                new_lines.append("    try:\n")
                new_lines.append("        loop.run_until_complete(main())\n")
                new_lines.append("    except (KeyboardInterrupt, SystemExit):\n")
                new_lines.append("        pass\n")
                changed = True
            else:
                new_lines.append(line)

        if changed:
            with open("rita_main.py", "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            logger.info("[INFO] ✅ rita_main.py: исправлен вызов asyncio.run(main()) на безопасный")
        else:
            logger.info("[INFO] ⚠️ rita_main.py: asyncio.run(main()) не найден — пропущено")
    except Exception as e:
        logger.info(f"[ERROR] ❌ Ошибка при замене asyncio.run: {e}")
def start_advanced_self_learning_thread():
    def thread_func():
        asyncio.run(run_self_improvement_cycle())
    threading.Thread(target=thread_func, daemon=True).start()
    log_info("🧩 Поток расширенного самообучения запущен")
import subprocess
import threading

def launch_rita_with_log():
    log_file_path = os.path.join(os.getcwd(), "log_errors.txt")

    with open(log_file_path, "a", encoding="utf-8") as log_file:
        process = subprocess.Popen(
            ["python3", "rita_main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        def log_output():
            for line in process.stdout:
                log_file.write(line)
                log_file.flush()
                if "telegram" in line.lower() or "conflict" in line.lower() or "error" in line.lower():
                    logger.info(f"[TELEGRAM LOG] {line.strip()}")  # Для быстрой отладки

        threading.Thread(target=log_output, daemon=True).start()
        return process

# Используем это вместо subprocess.Popen(["python3", "rita_main.py"])


# --- Константы и ключи ---
TELEGRAM_ADMIN_ID =    # твой Telegram ID

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
OWNER_TELEGRAM_ID = int(os.getenv("OWNER_TELEGRAM_ID", 0))

MAIN_SCRIPT_PATH = Path(__file__).parent / "rita_main.py"
DIAGNOSTICS_SCRIPT_PATH = Path(__file__).resolve()

LOG_FILE = Path(__file__).parent / "check_bot_diagnostics.log"
logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",
)
logger = logging.getLogger(__name__)

bot = Bot(token=TELEGRAM_BOT_TOKEN)

import os
import signal
import subprocess

import psutil
import os
import time
import signal

def kill_duplicate_rita_bots():
    current_pid = os.getpid()
    rita_main_path = os.path.abspath("rita_main.py")
    killed = 0

    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            pid = proc.info['pid']
            cmdline = proc.info['cmdline']

            if pid == current_pid:
                continue

            if cmdline and 'python' in cmdline[0] and rita_main_path in " ".join(cmdline):
                # Дополнительная проверка — оставить тот, кто запущен позже всех (последний)
                proc_create_time = proc.create_time()
                now = time.time()

                # Убиваем если работает больше 15 секунд (старый дубликат)
                if now - proc_create_time > 15:
                    os.kill(pid, signal.SIGTERM)
                    logger.info(f"[INFO] Завершён дубликат процесса {pid} (rita_main.py)")
                    killed += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if killed == 0:
        logger.info("[INFO] Дубликатов rita_main.py не обнаружено.")

kill_duplicate_rita_bots()

def check_and_fix_main_script():
    path = os.path.join(os.getcwd(), "rita_main.py")
    if not os.path.exists(path):
        logger.info("[ERROR] rita_main.py не найден для анализа")
        return

    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # Проверка отсутствия asyncio.run(main())
    if "asyncio.run(main())" not in code:
        logger.info("[FIX] Добавляем asyncio.run(main()) в конец rita_main.py")
        if "async def main(" in code:
            code += "\n\nif __name__ == '__main__':\n    import asyncio\n    asyncio.run(main())\n"
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)
            logger.info("✅ Исправление вставлено.")
        else:
            logger.info("[WARN] main() не найден в rita_main.py — пропускаем исправление.")
    else:
        logger.info("✅ asyncio.run(main()) уже присутствует — ничего не меняем.")

check_and_fix_main_script()

# Пути и настройки
from pathlib import Path
import requests
import time

LOG_FILE = Path("./check_bot_diagnostics.log")
MAIN_SCRIPT_PATH = Path("./rita_main.py")
HELPER_SCRIPT_PATH = Path("./check_bot_diagnostics.py")

REPO_RAW_URL = "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main"

# --- Логирование ---
def log_debug(msg):
    logger.info(f"[DEBUG] {time.ctime()} - {msg}")

def log_info(msg):
    logger.info(f"[INFO] {time.ctime()} - {msg}")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[INFO] {time.ctime()} - {msg}\n")
    except:
        pass

def log_error(msg):
    logger.info(f"[ERROR] {time.ctime()} - {msg}")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[ERROR] {time.ctime()} - {msg}\n")
    except:
        pass

# --- Автообновление скрипта ---
def auto_update_script(script_path: Path, repo_raw_url: str) -> bool:
    try:
        log_info(f"Попытка автообновления: {script_path.name}")
        raw_url = f"{repo_raw_url}/{script_path.name}"

        response = requests.get(raw_url, timeout=15)
        if response.status_code != 200:
            log_error(f"Не удалось скачать raw файл {script_path.name}, статус: {response.status_code}")
            return False

        new_code = response.text
        if script_path.exists():
            current_code = script_path.read_text(encoding="utf-8")
            if new_code == current_code:
                log_info(f"{script_path.name} уже актуален")
                return False
        # ... продолжение функции ...

        script_path.write_text(new_code, encoding="utf-8")
        log_info(f"{script_path.name} успешно обновлен")
        return True
    except Exception as e:
        log_error(f"Ошибка автообновления {script_path.name}: {e}")
        return False
import socket
import requests

def check_internet() -> bool:
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        log_info("Интернет доступен")
        return True
    except Exception as e:
        log_error(f"Ошибка соединения с интернетом: {e}")
        return False
def check_openai_api() -> bool:
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
        openai.Model.list()
        log_info("OpenAI API доступен")
        return True
    except Exception as e:
        log_error(f"Ошибка OpenAI API: {e}")
        return False

def check_hf_api() -> bool:
    try:
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        r = requests.get("https://api-inference.huggingface.co/models", headers=headers, timeout=10)
        if r.status_code == 200:
            log_info("HuggingFace API доступен")
            return True
        else:
            log_error(f"HuggingFace API ошибка, статус: {r.status_code}")
            return False
    except Exception as e:
        log_error(f"Ошибка HuggingFace API: {e}")
        return False

def check_google_search_api() -> bool:
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q=test"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            log_info("Google Custom Search API доступен")
            return True
        else:
            log_error(f"Google Search API ошибка, статус: {r.status_code}")
            return False
    except Exception as e:
        log_error(f"Google Search API исключение: {e}")
        return False

# --- Функция для подсчёта sha256 хеша файла ---
def calculate_hash(file_path: Path) -> str:
    try:
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        logger.error(f"Ошибка вычисления хеша {file_path}: {e}")
        return ""


from telegram import Update
from telegram.ext import ContextTypes

async def cmd_update_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("⛔ У вас нет доступа к этой команде.")
        return
    await update.message.reply_text("📥 Обновление rita_main.py...")

    repo_raw_url = "https://github.com/DeViLs9966/rita_mega_bot"
    updated = auto_update_script(MAIN_SCRIPT_PATH, repo_raw_url)

    if updated:
        await update.message.reply_text("✅ rita_main.py обновлён.")
    else:
        await update.message.reply_text("ℹ️ rita_main.py без изменений.")
async def cmd_update_self(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("⛔ У вас нет доступа к этой команде.")
        return
    await update.message.reply_text("📥 Обновление check_bot_diagnostics.py...")

    repo_raw_url = "https://github.com/DeViLs9966/rita_mega_bot"
    updated = auto_update_script(DIAGNOSTICS_SCRIPT_PATH, repo_raw_url)

    if updated:
        await update.message.reply_text("✅ check_bot_diagnostics.py обновлён.")
    else:
        await update.message.reply_text("ℹ️ Скрипт уже актуален.")


# — Отправка Telegram-сообщения —
async def send_telegram_message(text: str):
    try:
        await bot.send_message(chat_id=TELEGRAM_ADMIN_ID, text=text)
        log_info(f"Отправлено в Telegram: {text}")
    except Exception as e:
        log_error(f"Ошибка при отправке в Telegram: {e}")

# — Проверки подключения —
def check_internet(timeout=5) -> bool:
    try:
        response = requests.get("https://www.google.com", timeout=timeout)
        log_debug("Интернет доступен")
        return response.status_code == 200
    except requests.RequestException:
        log_error("Нет доступа к интернету")
        return False

def check_openai_api() -> bool:
    import openai
    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.Model.list()
        log_debug(f"OpenAI API доступен, моделей: {len(response.data)}")
        return True
    except Exception as e:
        log_error(f"OpenAI API ошибка: {e}")
        return False

def check_hf_api() -> bool:
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    try:
        r = requests.get("https://api-inference.huggingface.co/models", headers=headers, timeout=10)
        if r.status_code == 200:
            log_debug("HuggingFace API доступен")
            return True
        else:
            log_error(f"HuggingFace API ошибка, статус: {r.status_code}")
            return False
    except Exception as e:
        log_error(f"HuggingFace API исключение: {e}")
        return False

def check_google_search_api() -> bool:
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q=test"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            log_debug("Google Custom Search API доступен")
            return True
        else:
            log_error(f"Google Custom Search API ошибка, статус: {r.status_code}")
            return False
    except Exception as e:
        log_error(f"Google Search API исключение: {e}")
        return False

# — Автообновление скрипта (по raw ссылке GitHub) —
def auto_update_script(script_path: Path, repo_url: str):
    try:
        log_info(f"Попытка автообновления: {script_path.name}")
        if shutil.which("git") is not None:
            script_dir = script_path.parent
            if (script_dir / ".git").exists():
                log_debug(f"Выполняем git pull в {script_dir}")
                subprocess.run(["git", "-C", str(script_dir), "pull"], check=True)
                log_info(f"{script_path.name} обновлен через git pull")
                return True

        raw_url = repo_url.rstrip("/") + "/" + script_path.name
        log_debug(f"Скачиваем raw файл по URL: {raw_url}")
        r = requests.get(raw_url, timeout=15)
        if r.status_code == 200:
            script_path.write_text(r.text, encoding="utf-8")
            log_info(f"{script_path.name} обновлен скачиванием raw файла")
            return True
        else:
            log_error(f"Не удалось скачать raw файл, статус: {r.status_code}")
            return False
    except Exception as e:
        log_error(f"Ошибка автообновления: {e}")
        return False
# check_bot_diagnostics.py — БЛОК 2 из 6

import psutil
import platform
import threading
import hashlib

# — Команды Telegram-бота —

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Это вспомогательный модуль RITA AI.\n"
        "Доступные команды:\n"
        "/pro — системный отчёт\n"
        "/proverka — проверка API и ключей\n"
        "/update_main — обновление основного скрипта\n"
        "/update_self — обновление этого скрипта\n"
        "/restart — перезапуск бота"
    )

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Команды справки:\n"
        "/pro — полный системный отчёт\n"
        "/proverka — проверка API и ключей\n"
        "/update_main — обновить rita_main.py\n"
        "/update_self — обновить check_bot_diagnostics.py\n"
        "/restart — перезапуск скрипта (для владельца)"
    )

async def cmd_pro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        sys_info = platform.uname()
        text = (
            f"📊 Системный отчёт:\n"
            f"Процессор: {sys_info.processor}\n"
            f"Ядер: {cpu_count}\n"
            f"Частота: {cpu_freq.current:.2f} MHz\n"
            f"RAM: {ram.total // (1024**2)} MB (исп: {ram.used // (1024**2)} MB)\n"
            f"Диск: {disk.total // (1024**3)} GB (свободно: {disk.free // (1024**3)} GB)\n"
            f"OS: {sys_info.system} {sys_info.release}\n"
            f"Python: {platform.python_version()}"
        )
        await update.message.reply_text(text)
        log_debug("Выполнена команда /pro")
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка /pro: {e}")
        log_error(f"Ошибка в /pro: {e}")

async def cmd_proverka(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔎 Проверка ключей и API...")
    results = []
    if check_internet(): results.append("🌐 Интернет: OK")
    else: results.append("🌐 Интернет: ❌")

    if check_openai_api(): results.append("🤖 OpenAI API: OK")
    else: results.append("🤖 OpenAI API: ❌")

    if check_hf_api(): results.append("🧠 HuggingFace API: OK")
    else: results.append("🧠 HuggingFace API: ❌")

    if check_google_search_api(): results.append("🔍 Google Search API: OK")
    else: results.append("🔍 Google Search API: ❌")

    await update.message.reply_text("\n".join(results))
    log_debug("Выполнена команда /proverka")

async def cmd_update_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return
    await update.message.reply_text("📥 Обновление rita_main.py...")
    updated = auto_update_script(MAIN_SCRIPT_PATH, "https://raw.githubusercontent.com/yourusername/rita_mega_bot/main")
    if updated:
        await update.message.reply_text("✅ rita_main.py обновлён.")
    else:
        await update.message.reply_text("ℹ️ rita_main.py без изменений.")

async def cmd_update_self(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return
    await update.message.reply_text("📥 Обновление check_bot_diagnostics.py...")
    updated = auto_update_script(DIAGNOSTICS_SCRIPT_PATH, "https://raw.githubusercontent.com/yourusername/rita_mega_bot/main")
    if updated:
        await update.message.reply_text("✅ Скрипт обновлён.")
    else:
        await update.message.reply_text("ℹ️ Уже актуален.")

async def cmd_restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("⛔ Недостаточно прав.")
        return
    await update.message.reply_text("♻️ Перезапуск...")
    log_info("Перезапуск по команде владельца")
    os.execv(sys.executable, ['python3'] + sys.argv)

# — Мониторинг изменений хэшей файлов —

def calculate_hash(path: Path) -> str:
    try:
        content = path.read_bytes()
        return hashlib.sha256(content).hexdigest()
    except Exception as e:
        log_error(f"Ошибка хэша {path.name}: {e}")
        return ""

last_main_hash = ""
last_diag_hash = ""

def monitor_scripts_changes():
    global last_main_hash, last_diag_hash
    while True:
        time.sleep(300)  # 5 минут
        main_hash = calculate_hash(MAIN_SCRIPT_PATH)
        diag_hash = calculate_hash(HELPER_SCRIPT_PATH)
        if main_hash != last_main_hash:
            log_info("⚠️ Изменён основной скрипт!")
            last_main_hash = main_hash
        if diag_hash != last_diag_hash:
            log_info("⚠️ Изменён вспомогательный скрипт!")
            last_diag_hash = diag_hash

def start_monitoring_thread():
    thread = threading.Thread(target=monitor_scripts_changes, daemon=True)
    thread.start()
    log_info("🧩 Поток мониторинга изменений запущен")


    # Тут запускается asyncio loop или main bot handler


# --- Дополнительно в блок 2 после определения monitor_scripts_changes() ---

import asyncio

# Глобальные переменные для хранения последних хешей
last_main_hash = ""
last_diag_hash = ""

async def auto_fix_and_restart_if_needed():
    global last_main_hash, last_diag_hash
    while True:
        await asyncio.sleep(300)  # 5 минут

        current_main_hash = calculate_hash(MAIN_SCRIPT_PATH)
        current_diag_hash = calculate_hash(HELPER_SCRIPT_PATH)

        if current_main_hash != last_main_hash:
            last_main_hash = current_main_hash
            log_info("Обнаружено изменение rita_main.py, обновляем и перезапускаем")
            updated = auto_update_script(MAIN_SCRIPT_PATH, "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main")
            if updated:
                log_info("rita_main.py обновлен, перезапуск...")
                try:
                    subprocess.Popen([sys.executable, str(MAIN_SCRIPT_PATH)])
                    log_info("rita_main.py успешно запущен")
                except Exception as e:
                    log_error(f"Ошибка при перезапуске rita_main.py: {e}")

        if current_diag_hash != last_diag_hash:
            last_diag_hash = current_diag_hash
            log_info("Обнаружено изменение check_bot_diagnostics.py, обновляем...")
            updated = auto_update_script(HELPER_SCRIPT_PATH, "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main")
            if updated:
                log_info("check_bot_diagnostics.py обновлен")

        # Вычисляем текущие хеши
        current_main_hash = calculate_hash(MAIN_SCRIPT_PATH)
        current_diag_hash = calculate_hash(DIAGNOSTICS_SCRIPT_PATH)

        if current_main_hash != last_main_hash:
            last_main_hash = current_main_hash
            log_info("Обнаружено изменение в rita_main.py, пытаемся обновить и перезапустить")
            updated = auto_update_script(MAIN_SCRIPT_PATH, "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main")
            if updated:
                log_info("rita_main.py обновлен, перезапуск...")
                # Перезапускаем основной скрипт
                try:
                    subprocess.Popen([sys.executable, str(MAIN_SCRIPT_PATH)])
                    log_info("rita_main.py перезапущен успешно")
                except Exception as e:
                    log_error(f"Ошибка при перезапуске rita_main.py: {e}")

        if current_diag_hash != last_diag_hash:
            last_diag_hash = current_diag_hash
            log_info("Обнаружено изменение в check_bot_diagnostics.py, обновляемся...")
            updated = auto_update_script(DIAGNOSTICS_SCRIPT_PATH, "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main")
            if updated:
                log_info("check_bot_diagnostics.py обновлен")

# --- Логирование ---
def log_info(msg): logger.info(f"[INFO] {time.ctime()} - {msg}")
def log_error(msg): logger.info(f"[ERROR] {time.ctime()} - {msg}")

# check_bot_diagnostics.py — БЛОК 3 из 6

import logging
import requests
import json

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Лог-файл
LOG_FILE = 'rita_diagnostics.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def log_debug(msg):
    logging.debug(msg)

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)

# --- Проверка подключения к интернету ---
def check_internet(url='https://www.google.com') -> bool:
    try:
        r = requests.get(url, timeout=5)
        log_debug("Проверка интернета выполнена успешно")
        return r.status_code == 200
    except Exception as e:
        log_error(f"Ошибка при проверке интернета: {e}")
        return False

# --- Проверка OpenAI API (GPT) ---
def check_openai_api() -> bool:
    import openai
    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.Model.list()
        log_debug(f"OpenAI API доступен, моделей: {len(response.data)}")
        return True
    except Exception as e:
        log_error(f"OpenAI API ошибка: {e}")
        return False

# --- Проверка HuggingFace API ---
def check_hf_api() -> bool:
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    try:
        r = requests.get("https://api-inference.huggingface.co/models", headers=headers, timeout=10)
        if r.status_code == 200:
            log_debug("HuggingFace API доступен")
            return True
        else:
            log_error(f"HuggingFace API ошибка, статус: {r.status_code}")
            return False
    except Exception as e:
        log_error(f"HuggingFace API исключение: {e}")
        return False

# --- Проверка Google Search API ---1
def check_google_search_api():
    try:
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CX,
            "q": "test"
        }
        r = requests.get("https://www.googleapis.com/customsearch/v1", params=params, timeout=10)
        if r.status_code == 200:
            log_info("Google Search API работает")
            return True
        else:
            log_error(f"Google API ошибка: {r.status_code}, {r.text}")
            return False
    except Exception as e:
        log_error(f"Google Search API исключение: {e}")
        return False

# --- Обновление скрипта из GitHub ---
def auto_update_script(script_path, repo_url):
    try:
        filename = script_path.name
        raw_url = f"{repo_url}/{filename}"
        log_info(f"Получение кода из {raw_url}")
        response = requests.get(raw_url, timeout=15)
        if response.status_code == 200:
            new_code = response.text
            current_code = script_path.read_text(encoding='utf-8')
            if new_code != current_code:
                script_path.write_text(new_code, encoding='utf-8')
                log_info(f"{filename} обновлён.")
                return True
            else:
                log_info(f"{filename} уже актуален.")
                return False
        else:
            log_error(f"Ошибка загрузки {filename}: HTTP {response.status_code}")
            return False
    except Exception as e:
        log_error(f"Ошибка автообновления {script_path.name}: {e}")
        return False
# check_bot_diagnostics.py — блок 4 из 6 (полный и расширенный)

import os
import threading
import hashlib
import time
from pathlib import Path
from telegram import Bot
from telegram.ext import ContextTypes

# Ключи и настройки (вставь свои реальные)
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
OWNER_TELEGRAM_ID = int(os.getenv("OWNER_TELEGRAM_ID", 0))

MAIN_SCRIPT_PATH = Path("./rita_main.py")
HELPER_SCRIPT_PATH = Path("./check_bot_diagnostics.py")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# === Лог-функции из блока 1 ===
def log_info(msg):
    logger.info(f"[INFO] {time.ctime()} - {msg}")

def log_error(msg):
    logger.info(f"[ERROR] {time.ctime()} - {msg}")

# Функция хеширования файла (для проверки целостности)
def calculate_hash(file_path: Path) -> str:
    try:
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        log_error(f"Ошибка вычисления хеша файла {file_path}: {e}")
        return ""

# Защита от несанкционированного доступа по ID
def is_authorized(user_id: int) -> bool:
    return user_id == TELEGRAM_ADMIN_ID

# Обработка команды /pro — расширенная проверка систем и уведомление админа
async def handle_command_pro(update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="У вас нет доступа к этой команде.")
        log_info(f"Автообновления: попытка доступа к /pro от неавторизованного пользователя {user_id}")
        return

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Запущена расширенная диагностика системы...")
    log_info("Запущена команда /pro")

    # Проверки
    internet_ok = check_internet()
    openai_ok = check_openai_api()
    hf_ok = check_hf_api()
    google_ok = check_google_search_api()
    main_script_hash = calculate_hash(MAIN_SCRIPT_PATH)

    report = (
        f"Диагностика системы:\n"
        f"Интернет: {'OK' if internet_ok else 'Проблемы'}\n"
        f"OpenAI API: {'OK' if openai_ok else 'Проблемы'}\n"
        f"HuggingFace API: {'OK' if hf_ok else 'Проблемы'}\n"
        f"Google Search API: {'OK' if google_ok else 'Проблемы'}\n"
        f"Хеш основного скрипта: {main_script_hash}\n"
        f"Время: {time.ctime()}"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=report)
    log_info("Диагностический отчет отправлен.")

# Обработка команды /proverka — проверка и исправление (самообновление)
# Функция обработки команды /proverka — проверка и обновление скриптов
async def handle_command_proverka(update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_TELEGRAM_ID:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="⛔ У вас нет доступа к этой команде.")
        log_info(f"Попытка доступа к /proverka от неавторизованного пользователя {user_id}")
        return

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Запущена проверка и обновление скриптов...")

    repo_raw_url = "https://github.com/DeViLs9966/rita_mega_bot"
    updated_main = auto_update_script(MAIN_SCRIPT_PATH, repo_raw_url)
    updated_helper = auto_update_script(HELPER_SCRIPT_PATH, repo_raw_url)

    msg = "Обновление завершено:\n"
    msg += f"Основной скрипт: {'обновлён' if updated_main else 'без изменений'}\n"
    msg += f"Вспомогательный скрипт: {'обновлён' if updated_helper else 'без изменений'}"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    log_info("Команда /proverka выполнена, результат отправлен администратору.")

# Функция
# сообщения админуотправки сообщений админу из любого места скрипта
import asyncio

# Объявляем TELEGRAM_ADMIN_ID где-то глобально, например:
TELEGRAM_ADMIN_ID =    # или берёшь из конфига/переменных окружения

# Инициализация бота (уже должна быть в коде)
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Асинхронная функция для отправки сообщения админу
async def send_admin_message(text: str):
    try:
        await bot.send_message(chat_id=TELEGRAM_ADMIN_ID, text=text)
        logger.info(f"Отправлено сообщение админу: {text}")
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения админу: {e}")

# Чтобы вызвать из синхронного кода (например, из потока или цикла):
def send_admin_message_sync(text: str):
    asyncio.run(send_admin_message(text))

# Исправленный периодический отчёт (запускаем в отдельном потоке и с async вызовом)
def start_periodic_report(interval_seconds=3600):
    async def report_loop():
        while True:
            internet_status = "OK" if check_internet() else "OFF"
            message = f"[Отчёт] Система работает. Интернет: {internet_status}. Время: {time.ctime()}"
            await send_admin_message(message)
            await asyncio.sleep(interval_seconds)

    def start_loop():
        asyncio.run(report_loop())

    threading.Thread(target=start_loop, daemon=True).start()
    log_info("Запущена периодическая рассылка отчётов админу")

# Функция perform_self_learning из блока 2 (расширенная диагностика и самообучение)
import openai
import asyncio
from pathlib import Path

# Лог-функции (пример, можно использовать свои)
def log_info(msg):
    logger.info(f"[INFO] {msg}")

def log_error(msg):
    logger.info(f"[ERROR] {msg}")

# Ключ OpenAI
OPENAI_API_KEY = "твой_ключ_отсюда_или_через_env"

# Пути к скриптам и логу
MAIN_SCRIPT_PATH = Path("rita_main.py")
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
LOG_FILE_PATH = Path("check_bot_diagnostics.log")

async def generate_fix_patch(error_log_snippet: str, file_content: str) -> str:
    """
    Отправляет запрос в OpenAI для генерации исправленного кода на основе лога ошибок и текущего кода.
    Возвращает исправленный полный код.
    """
    prompt = (
        "В этом фрагменте лога ошибок:\n"
        f"{error_log_snippet}\n"
        "Предложи исправления для следующего кода:\n"
        f"{file_content}\n"
        "Верни исправленный полный код без объяснений."
    )
    try:
        openai.api_key = OPENAI_API_KEY
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=1500,
        )
        fixed_code = response.choices[0].message.content.strip()
        return fixed_code
    except Exception as e:
        log_error(f"Ошибка вызова OpenAI для исправления кода: {e}")
        return ""


async def analyze_and_fix_script(script_path: Path, log_path: Path = LOG_FILE_PATH) -> bool:
    """
    Анализирует последние ошибки из лога и пытается исправить скрипт,
    перезаписывая файл, если OpenAI предлагает изменения.
    Возвращает True, если код был обновлен, иначе False.
    """
    try:
        if not log_path.exists() or not script_path.exists():
            log_info(f"Файл лога или скрипта не найден: {log_path}, {script_path}")
            return False

        # Читаем последние 100 строк логов и фильтруем ошибки
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        error_lines = [line for line in lines if "[ERROR]" in line]
        last_errors = "".join(error_lines[-50:]) if error_lines else ""

        if not last_errors:
            log_info("Ошибок для анализа не найдено, пропускаем исправление")
            return False

        # Читаем текущий код скрипта
        current_code = script_path.read_text(encoding="utf-8")

        # Запрашиваем исправления у OpenAI
        fixed_code = await generate_fix_patch(last_errors, current_code)

        if fixed_code and fixed_code != current_code:
            backup_path = script_path.with_suffix(script_path.suffix + ".bak")
            script_path.replace(backup_path)
            log_info(f"Создана резервная копия: {backup_path}")

            script_path.write_text(fixed_code, encoding="utf-8")
            log_info(f"Автоматически применены исправления для {script_path.name}")
            return True
        else:
            log_info(f"Исправления не были предложены или совпадают с текущим кодом для {script_path.name}")
            return False

    except Exception as e:
        log_error(f"Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False

        # Читаем последние 100 строк логов и фильтруем ошибки
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        error_lines = [line for line in lines if "[ERROR]" in line]
        last_errors = "".join(error_lines[-50:]) if error_lines else ""

        if not last_errors:
            log_info("Ошибок для анализа не найдено, пропускаем исправление")
            return False

        # Читаем текущий код скрипта
        current_code = script_path.read_text(encoding="utf-8")

        # Запрашиваем исправления у OpenAI
        fixed_code = await generate_fix_patch(last_errors, current_code)

        if fixed_code and fixed_code != current_code:
            # Создаем резервную копию
            backup_path = script_path.with_suffix(script_path.suffix + ".bak")
            script_path.replace(backup_path)
            log_info(f"Создана резервная копия: {backup_path}")

            # Записываем исправленный код
            script_path.write_text(fixed_code, encoding="utf-8")
            log_info(f"✅ Автоматически применены исправления для {script_path.name}")
            return True
        else:
            log_info(f"⚠️ Исправления не были предложены или совпадают с текущим кодом для {script_path.name}")
            return False

    except Exception as e:
        log_error(f"❌ Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False

        # Запрашиваем исправления у OpenAI
        fixed_code = await generate_fix_patch(last_errors, current_code)

        if fixed_code and fixed_code != current_code:
            backup_path = script_path.with_suffix(script_path.suffix + ".bak")
            script_path.replace(backup_path)
            log_info(f"Создана резервная копия: {backup_path}")

            script_path.write_text(fixed_code, encoding="utf-8")
            log_info(f"Автоматически применены исправления для {script_path.name}")
            return True
        else:
            log_info(f"Исправления не были предложены или совпадают с текущим кодом для {script_path.name}")
            return False

    except Exception as e:
        log_error(f"Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False

        # Читаем текущий код скрипта
        current_code = script_path.read_text(encoding="utf-8")

        # Запрашиваем исправления у OpenAI
        fixed_code = await generate_fix_patch(last_errors, current_code)

        if fixed_code and fixed_code != current_code:
            # Создаем резервную копию
            backup_path = script_path.with_suffix(script_path.suffix + ".bak")
            script_path.replace(backup_path)
            log_info(f"Создана резервная копия: {backup_path}")

            # Записываем исправленный код
            script_path.write_text(fixed_code, encoding="utf-8")
            log_info(f"Автоматически применены исправления для {script_path.name}")
            return True
        else:
            log_info(f"Исправления не были предложены или совпадают с текущим кодом для {script_path.name}")
            return False

    except Exception as e:
        log_error(f"Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False

    except Exception as e:
        log_error(f"Ошибка в analyze_and_fix_script для {script_path.name}: {e}")
        return False
import psutil  # убедись, что установлен: pip install psutil

def monitor_main_script(interval=60):
    """
    Проверяет каждые `interval` секунд, запущен ли основной скрипт.
    Если нет — запускает его снова.
    """
    def loop():
        while True:
            main_running = False
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    if "rita_main.py" in " ".join(proc.info['cmdline']):
                        main_running = True
                        break
                except Exception:
                    continue

            if not main_running:
                log_error("Основной скрипт rita_main.py не найден. Перезапускаем...")
                try:
                    subprocess.Popen([sys.executable, str(MAIN_SCRIPT_PATH)])
                    send_admin_message_sync("⚠️ rita_main.py был автоматически перезапущен (не обнаружен в процессе).")
                except Exception as e:
                    log_error(f"Не удалось перезапустить rita_main.py: {e}")

            time.sleep(interval)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    log_info("🩺 Запущен мониторинг процесса rita_main.py")

async def run_self_improvement_cycle():
    """
    Запускает полный цикл самоулучшения:
    - Анализирует ошибки,
    - Автообновляет скрипты из репозитория,
    - Автоматически исправляет скрипты с помощью OpenAI,
    - Перезапускает основной скрипт при необходимости,
    - Отправляет отчеты администратору.
    """
    try:
        error_report = analyze_errors_for_self_learning()  # должна быть функция из твоего кода
        await send_admin_message(error_report)            # должна быть асинхронная функция отправки в Telegram

        repo_raw_url = "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main"
        updated_main = auto_update_script(MAIN_SCRIPT_PATH, repo_raw_url)
        updated_helper = auto_update_script(HELPER_SCRIPT_PATH, repo_raw_url)

        fixed_main = await analyze_and_fix_script(MAIN_SCRIPT_PATH)
        fixed_helper = await analyze_and_fix_script(HELPER_SCRIPT_PATH)

        if updated_main or fixed_main:
            await restart_main_script()  # асинхронная функция для перезапуска основного скрипта

        if updated_helper or fixed_helper:
            await send_admin_message("🛠 check_bot_diagnostics.py был обновлен или исправлен.")

        log_info("✅ Цикл самоулучшения завершён.")
    except Exception as e:
        log_error(f"❌ Ошибка в цикле самоулучшения: {e}")

# check_bot_diagnostics.py — БЛОК 5 из 6

import subprocess
import sys
import json
import requests
import socket

# Повторно: лог-файл
LOG_FILE = Path("./diagnostics.log")

def log_error(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"[ERROR] {time.ctime()}: {message}\n")
    logger.info(f"[ERROR] {message}")

def log_info(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"[INFO] {time.ctime()}: {message}\n")
    logger.info(f"[INFO] {message}")

# --- Самообучение: анализ логов ---
def analyze_errors_for_self_learning() -> str:
    if not LOG_FILE.exists():
        return "Лог файл не найден для анализа."

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        error_lines = [line for line in lines if "[ERROR]" in line]
        recent_errors = error_lines[-100:]
        error_summary = {}

        for err in recent_errors:
            key = err.strip()
            error_summary[key] = error_summary.get(key, 0) + 1

        sorted_errors = sorted(error_summary.items(), key=lambda x: x[1], reverse=True)

        report = "📋 Отчёт самообучения (частота ошибок):\n"
        for err, count in sorted_errors[:10]:
            report += f"{count} раз: {err}\n"

        return report
    except Exception as e:
        log_error(f"Ошибка анализа логов: {e}")
        return "Ошибка при анализе логов."

# --- Обновление скрипта с GitHub ---
# --- Обновление скрипта с GitHub ---
def auto_update_script(script_path: Path, repo_raw_url: str) -> bool:
    try:
        log_info(f"Попытка автообновления: {script_path.name}")

        # Проверка, есть ли git и репозиторий
        if shutil.which("git") is not None:
            script_dir = script_path.parent
            git_folder = script_dir / ".git"
            if git_folder.exists():
                log_info(f"Выполняем git pull в {script_dir}")
                subprocess.run(["git", "-C", str(script_dir), "pull"], check=True)
                log_info(f"{script_path.name} обновлен через git pull")
                return True

        # Если git нет или не репозиторий — скачиваем raw файл
        raw_url = repo_raw_url.rstrip("/") + "/" + script_path.name
        log_info(f"Скачиваем raw файл по URL: {raw_url}")
        response = requests.get(raw_url, timeout=15)

        if response.status_code == 200:
            new_code = response.text
            current_code = ""
            if script_path.exists():
                current_code = script_path.read_text(encoding="utf-8")
            if new_code != current_code:
                script_path.write_text(new_code, encoding="utf-8")
                log_info(f"{script_path.name} обновлен скачиванием raw файла")
                return True
            else:
                log_info(f"{script_path.name} уже актуален")
                return False
        else:
            log_error(f"Не удалось скачать raw файл, статус: {response.status_code}")
            return False

    except Exception as e:
        log_error(f"Ошибка автообновления {script_path.name}: {e}")
        return False

# --- Перезапуск основного скрипта ---
async def restart_main_script():
    try:
        logger.info("🔁 Перезапуск основного скрипта rita_main.py")
        process = await asyncio.create_subprocess_exec(sys.executable, str(MAIN_SCRIPT_PATH))
        await send_admin_message("rita_main.py был автоматически перезапущен.")
    except Exception as e:
        logger.error(f"Ошибка перезапуска основного скрипта: {e}")

# --- Получение версии скрипта (если указана в начале файла) ---
def get_script_version(script_path: Path) -> str:
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            first_line = f.readline()
        if first_line.startswith("# Version:"):
            return first_line.strip().split(":")[1].strip()
        return "unknown"
    except Exception as e:
        log_error(f"Ошибка получения версии {script_path.name}: {e}")
        return "error"
async def background_error_log_analysis():
    while True:
        try:
            # Путь к логу, замени при необходимости
            log_file = "rita_bot.log"
            with open(log_file, "r", encoding="utf-8") as f:
                log_text = f.read()
            errors = parse_error_logs(log_text)
            if errors:
                fixes = generate_fixes_for_errors(errors)
                if fixes:
                    apply_fixes(fixes)
                    await send_admin_message(f"🛠 Автоматические исправления применены: {fixes}")
            await asyncio.sleep(300)  # Пауза 5 минут между проверками
        except Exception as e:
            logger.info(f"[ERROR] Ошибка в background_error_log_analysis: {e}")
            await asyncio.sleep(60)


# --- Полный цикл самообучения и автообновления ---
async def run_self_improvement_cycle():
    try:
        error_report = analyze_errors_for_self_learning()
        await send_admin_message(error_report)

        repo_raw_url = "https://github.com/DeViLs9966/rita_mega_bot"
        updated_main = auto_update_script(MAIN_SCRIPT_PATH, repo_raw_url)
        updated_helper = auto_update_script(HELPER_SCRIPT_PATH, repo_raw_url)

        if updated_main:
            await restart_main_script()

        if updated_helper:
            await send_admin_message("🛠 check_bot_diagnostics.py обновлён.")

        logger.info("✅ Цикл самоулучшения завершён.")
    except Exception as e:
        logger.error(f"❌ Ошибка в цикле самообучения: {e}")

# --- Проверки доступа к API и интернету ---
def check_openai_api() -> bool:
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
        openai.Model.list()
        return True
    except Exception as e:
        log_error(f"Ошибка OpenAI API: {e}")
        return False
def check_hf_api() -> bool:
    try:
        headers = {
            "Authorization": f"Bearer {HF_API_KEY}"
        }
        r = requests.get("https://api-inference.huggingface.co/models", headers=headers, timeout=10)
        return r.status_code == 200
    except Exception as e:
        log_error(f"Ошибка HuggingFace API: {e}")
        return False

def check_google_search_api() -> bool:
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q=test"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            log_debug("Google Custom Search API доступен")
            return True
        else:
            log_error(f"Google Custom Search API ошибка, статус: {r.status_code}")
            return False
    except Exception as e:
        log_error(f"Google Search API исключение: {e}")
        return False

def check_internet() -> bool:
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except Exception as e:
        log_error(f"Ошибка соединения с интернетом: {e}")
        return False
# check_bot_diagnostics.py — БЛОК 6 из 6 (ФИНАЛ)

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import asyncio
import signal
import sys
import subprocess
import shutil
from pathlib import Path

# ⬇️ Обязательные импорты из других частей
from logging import getLogger
logger = getLogger(__name__)

# Проверка Telegram ID
def is_authorized(user_id: int) -> bool:
    return user_id == TELEGRAM_ADMIN_ID

# --- Команды ---
async def cmd_pro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_authorized(update.effective_user.id):
        await update.message.reply_text("🔍 Запуск ручной диагностики и самообучения...")
        await asyncio.to_thread(run_self_improvement_cycle)
        await update.message.reply_text("✅ Диагностика и автообновление завершены.")
    else:
        await update.message.reply_text("⛔ У вас нет прав на выполнение этой команды.")

async def cmd_proverka(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_authorized(update.effective_user.id):
        report = analyze_errors_for_self_learning()
        await update.message.reply_text(f"📑 Анализ логов:\n{report}")
    else:
        await update.message.reply_text("⛔ У вас нет прав на выполнение этой команды.")

# --- Фоновое автообновление/обучение ---
async def periodic_self_improve():
    while True:
        try:
            await run_self_improvement_cycle()  # <- Добавляем await
        except Exception as e:
            log_error(f"Ошибка в периодическом цикле самоулучшения: {e}")
        await asyncio.sleep(1800)  # 30 минут

# --- Главная асинхронная функция ---
fix_rita_main_asyncio_run()
async def main():
    log_info("🚀 Запуск скрипта диагностики RITA AI")

    if not TELEGRAM_BOT_TOKEN:
        log_error("❌ TELEGRAM_BOT_TOKEN не задан. Прекращение работы.")
        sys.exit(1)

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Регистрация команд
    app.add_handler(CommandHandler("pro", cmd_pro))
    app.add_handler(CommandHandler("proverka", cmd_proverka))
    app.add_handler(CommandHandler("update_main", cmd_update_main))
    app.add_handler(CommandHandler("update_self", cmd_update_self))

    # Фоновые задачи
    asyncio.create_task(periodic_self_improve())
    start_monitoring_thread()
    start_advanced_self_learning_thread()
    start_periodic_report()

    asyncio.create_task(auto_fix_and_restart_if_needed())
    await app.run_polling()

# --- Обработка Ctrl+C / SIGTERM ---
def handle_exit(signal_received, frame):
    log_info("📴 Скрипт завершён пользователем (Ctrl+C)")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# --- Автообновление из GitHub ---
def auto_update_from_git():
    try:
        repo_dir = Path(__file__).parent
        if shutil.which("git"):
            subprocess.run(["git", "-C", str(repo_dir), "pull"], check=True)
            logger.info("✅ Автообновление из GitHub выполнено")
    except Exception as e:
        logger.info(f"❌ Автообновление из GitHub не удалось: {e}")

import re
import asyncio
import os
import time
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

LOG_FILE_PATH = "rita_bot.log"  # путь к файлу логов, где скрипт пишет ошибки
MAIN_SCRIPT_PATH = Path("rita_main.py")
DIAGNOSTIC_SCRIPT_PATH = Path("check_bot_diagnostics.py")


def parse_errors_from_log(log_path=LOG_FILE_PATH):
    """
    Считываем логи и извлекаем ошибки и предупреждения.
    Возвращаем список строк с описаниями ошибок.
    """
    errors = []
    error_patterns = [
        re.compile(r"ERROR\s*-\s*(.+)"),            # общий формат ошибки
        re.compile(r"Exception.*:\s*(.+)"),         # исключения
        re.compile(r"Traceback most recent call last:"),  # начало трассировки ошибок
        re.compile(r"Conflict: terminated by other getUpdates request;"),  # Telegram bot conflict
        # Можно добавить другие паттерны ошибок
    ]

    try:
        with open(log_path, "r", encoding="utf-8") as log_file:
            lines = log_file.readlines()

        buffer = []
        capture_traceback = False
        for line in lines:
            line = line.strip()
            if any(p.search(line) for p in error_patterns):
                buffer.append(line)
                if "Traceback" in line:
                    capture_traceback = True
                continue
            if capture_traceback:
                buffer.append(line)
                if line == "":
                    # конец трассировки
                    errors.append("\n".join(buffer))
                    buffer.clear()
                    capture_traceback = False
            else:
                # если в буфере что-то накопилось и дальше пусто — добавим
                if buffer:
                    errors.append("\n".join(buffer))
                    buffer.clear()
        if buffer:
            errors.append("\n".join(buffer))
    except Exception as e:
        logger.error(f"Ошибка чтения логов: {e}")
    return errors


def generate_fixes(errors):
    """
    На основе списка ошибок формируем предложения по исправлению.
    Возвращаем словарь: ключ — название скрипта, значение — текст исправления.
    """
    fixes = {
        "rita_main.py": [],
        "check_bot_diagnostics.py": []
    }

    for err in errors:
        if "asyncio.run(main())" in err:
            fixes["rita_main.py"].append(
                "# Исправлено: вызов asyncio.run(main()) обёрнут в защиту от запуска в уже запущенном event loop\n"
                "if __name__ == '__main__':\n"
                "    import asyncio\n"
                "    try:\n"
                "        asyncio.run(main())\n"
                "    except RuntimeError as e:\n"
                "        if 'event loop is running' in str(e):\n"
                "            import nest_asyncio\n"
                "            nest_asyncio.apply()\n"
                "            asyncio.run(main())\n"
                "        else:\n"
                "            raise\n"
            )
        elif "Conflict: terminated by other getUpdates request" in err:
            fixes["check_bot_diagnostics.py"].append(
                "# Исправлено: добавлена проверка и завершение дубликатов процессов, чтобы не было конфликтов Telegram bot\n"
                "def kill_existing_rita_bot():\n"
                "    import psutil\n"
                "    import os\n"
                "    current_pid = os.getpid()\n"
                "    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):\n"
                "        if proc.info['cmdline'] and 'rita_main.py' in ' '.join(proc.info['cmdline']) and proc.pid != current_pid:\n"
                "            logger.info(f'[INFO] Завершаю дубликат процесса {proc.pid} (rita_main.py)')\n"
                "            proc.kill()\n"
            )
        # Добавляй свои правила для других ошибок

    # Убираем дублирующие исправления, если есть
    for key in fixes:
        fixes[key] = list(set(fixes[key]))

    return fixes


def apply_fixes(fixes):
    """
    Вносит исправления в соответствующие скрипты.
    Возвращает список сообщений о проделанной работе.
    """
    results = []
    for script, fix_list in fixes.items():
        if not fix_list:
            continue
        try:
            path = Path(script)
            if not path.exists():
                results.append(f"[ERROR] {script} не найден для исправления.")
                continue
            with open(path, "a", encoding="utf-8") as f:
                f.write("\n\n# --- Автоматически добавленные исправления по результатам диагностики ---\n")
                for fix in fix_list:
                    f.write("\n" + fix + "\n")
            results.append(f"[INFO] Внесены исправления в {script}.")
        except Exception as e:
            results.append(f"[ERROR] Ошибка при записи в {script}: {e}")
    return results


async def auto_fix_from_logs():
    """
    Главная функция — анализируем логи, генерируем и применяем исправления.
    Отправляем отчет админу.
    """
    errors = parse_errors_from_log()
    if not errors:
        logger.info("Ошибок в логах не обнаружено, исправления не требуются.")
        return

    fixes = generate_fixes(errors)
    if not any(fixes.values()):
        logger.info("Не найдено подходящих исправлений для текущих ошибок.")
        return

    results = apply_fixes(fixes)
    for line in results:
        logger.info(line)

    # Можно отправить отчет в Telegram, если есть функция send_admin_message
    if 'send_admin_message' in globals():
        report = "\n".join(results)
        await send_admin_message(f"Автоматические исправления применены:\n{report}")


# Для запуска в asyncio
# Для запуска в asyncio
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import Conflict

nest_asyncio.apply()

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Привет! Я готов к работе.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✉️ Вы сказали: " + update.message.text)

async def run_bot():
    try:
        app = (
            ApplicationBuilder()
            .token(TELEGRAM_BOT_TOKEN)
            .concurrent_updates(True)
            .build()
        )

        app.add_handler(CommandHandler("start", start_handler))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

        logger.info("[✅] Бот запущен и работает.")
        await app.run_polling()

    except Conflict as e:
        logger.info(f"⚠️ Конфликт запуска: {e}")
        logger.info("⏳ Перезапуск через 10 секунд...")
        await asyncio.sleep(10)
        await run_bot()

    except Exception as e:
        logger.info(f"❌ Ошибка запуска бота: {e}")

async def main_entry():
    log_info("[INFO] Запуск автофикса из логов...")
    await auto_fix_from_logs()

    log_info("[INFO] Старт фоновых задач автообновления и мониторинга...")
    asyncio.create_task(auto_fix_loop())
    asyncio.create_task(auto_fix_and_restart_if_needed())
    start_monitoring_thread()

    log_info("[INFO] Запуск Telegram-бота...")
    await run_bot()

if __name__ == "__main__":
    asyncio.run(main_entry())
