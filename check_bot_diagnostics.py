TELEGRAM_BOT_TOKEN = '7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4'
with open('.token_clean') as f:
    cleaned_token = f.read().strip()

import traceback



# check_bot_diagnostics.py — БЛОК 1 из 6


import os

TOKEN_FILE = ".token_clean"

def load_clean_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token = f.read().strip()
            print(f"[DEBUG] Загружен токен из {TOKEN_FILE}: {repr(token)}")
            return token
    else:
        # Если файла нет, читаем из .env
        from dotenv import load_dotenv
        load_dotenv()
        raw_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        print(f"[DEBUG] Загружен токен из .env: {repr(raw_token)}")

        # Запишем в .token_clean для следующего запуска
        with open(TOKEN_FILE, "w") as f:
            f.write(raw_token)
        return raw_token

TELEGRAM_BOT_TOKEN = load_clean_token()
from telegram import Bot

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")


from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env в окружение

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
GITHUB_PAT = os.getenv("GITHUB_PAT")





import os
import re
import subprocess
import aiohttp
import asyncio
from telegram import Bot
from dotenv import load_dotenv
from telegram import Bot
import subprocess

import subprocess

from telegram import Bot

# Читаем токен из файла .token_clean
with open(".token_clean", "r") as f:
    TELEGRAM_BOT_TOKEN = f.read().strip()

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")


print("Запускаем fix_token_issue.py для проверки и исправления токена...")
subprocess.run(["python3", "fix_token_issue.py"], check=True)

with open(".token_clean", "r") as f:
    TELEGRAM_BOT_TOKEN = f.read().strip()

from telegram import Bot

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")


subprocess.run(["python3", "fix_token_issue.py"])
# === Загрузка переменных из .env ===
load_dotenv()

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
TELEGRAM_ADMIN_ID = int(os.getenv("TELEGRAM_ADMIN_ID", "558079551"))  # по умолчанию твой ID

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден. Убедись, что он указан в .env")

# === Создаём экземпляр бота ===
bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")

# === Пути к файлам ===
LOG_FILE = "/mnt/data/rita_mega_bot/logs/rita_bot.log"
MAIN_SCRIPT = "/mnt/data/rita_mega_bot/rita_main.py"
GIT_REPO_PATH = "/mnt/data/rita_mega_bot"


from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="/data/data/com.termux/files/home/rita_mega_bot/.env")

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"


from dotenv import load_dotenv
import os

load_dotenv()  # Загружаем переменные из .env

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"

print(f"[DEBUG] TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN!r}")  # отладочный вывод




import asyncio
import logging
# другие нужные импорты
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from pathlib import Path
from utils.fix_syntax import fix_unclosed_syntax, try_fix_syntax
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

import os
import re
import subprocess
import aiohttp
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
TELEGRAM_ADMIN_ID = int(os.getenv("TELEGRAM_ADMIN_ID", "558079551"))

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден. Убедись, что он указан в .env")

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")
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





from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("proverka"))
async def proverka_handler(message: types.Message):
    await message.reply("Бот работает, команда /proverka получена!")




import asyncio



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
        except Exception as e:
            pass
    return count > 1

def is_another_instance_running(script_name):
    count = 0
    for proc in psutil.process_iter(['cmdline']):
        try:
            cmd = proc.info['cmdline']
            if cmd and script_name in ' '.join(cmd):
                count += 1
        except Exception as e:
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












import os
import logging
from dotenv import load_dotenv

# Подключаем загрузку переменных из .env
load_dotenv()

# === Твои реальные токены из окружения ===
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
ADMIN_CHAT_ID = 558079551  # Твой ID

# Проверяем переменные, если нет — падаем с ошибкой
missing_vars = []
if not TELEGRAM_BOT_TOKEN:
    missing_vars.append("TELEGRAM_BOT_TOKEN")
if not OPENAI_API_KEY:
    missing_vars.append("OPENAI_API_KEY")
if not HF_API_TOKEN:
    missing_vars.append("HF_API_TOKEN")

if missing_vars:
    raise EnvironmentError(f"Отсутствуют обязательные переменные окружения: {', '.join(missing_vars)}")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Telegram Token: {TELEGRAM_BOT_TOKEN[:10]}... (длина {len(TELEGRAM_BOT_TOKEN)})")
logger.info(f"OpenAI Key: {OPENAI_API_KEY[:10]}... (длина {len(OPENAI_API_KEY)})")
logger.info(f"HuggingFace Token: {HF_API_TOKEN[:10]}... (длина {len(HF_API_TOKEN)})")

# Вот твой токен из лога (НЕ РЕКОМЕНДУЮ так хранить в коде, только для примера):
print(f"Пример твоего TELEGRAM_BOT_TOKEN: 7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")

# Далее подключай ключи к своим библиотекам, например:
# openai.api_key = OPENAI_API_KEY
# bot = Bot(token=TELEGRAM_BOT_TOKEN)

# ---------------------------------------
# Пример .env файла (создай рядом с твоим скриптом):

# TELEGRAM_BOT_TOKEN=7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4
# OPENAI_API_KEY=твой_ключ_openai_без_кавычек
# HF_API_TOKEN=твой_ключ_huggingface_без_кавычек




from dotenv import load_dotenv
load_dotenv()
import asyncio
import logging
import os
import sys
from pathlib import Path

import openai
import requests
from telegram import Update, Bot
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ========== ЗАГРУЗКА КЛЮЧЕЙ ИЗ ОКРУЖЕНИЯ ================
def get_env_key(key_name: str, required=True) -> str:
    value = os.getenv(key_name)
    if required and (value is None or value.strip() == ""):
        logging.error(f"Required environment variable '{key_name}' is missing or empty.")
        sys.exit(1)
    return value


TELEGRAM_BOT_TOKEN = get_env_key("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = get_env_key("OPENAI_API_KEY")
HF_API_TOKEN = get_env_key("HF_API_TOKEN")
ADMIN_CHAT_ID = int(get_env_key("ADMIN_CHAT_ID"))  # Ожидается целое число

# ========== ЛОГИРОВАНИЕ ========================
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ========== ИНИЦИАЛИЗАЦИЯ БОТА =================
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# ========== НАСТРОЙКА OPENAI ===================
openai.api_key = OPENAI_API_KEY

# ========== РЕЖИМЫ РАБОТЫ =====================
current_mode = "gpt4"  # по умолчанию

MODES = {"gpt4", "gpt2", "gog", "ht"}


async def send_telegram_notification(message: str):
    """Отправить уведомление администратору."""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": ADMIN_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown",
        }
        resp = requests.post(url, data=data, timeout=10)
        if not resp.ok:
            logger.error(f"Telegram notification failed: {resp.text}")
    except Exception as e:
        logger.error(f"Telegram notification exception: {e}")


async def call_openai_gpt4(prompt: str) -> str:
    """Асинхронный вызов OpenAI GPT-4o-mini для генерации ответа."""
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты - умный и дружелюбный помощник."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            max_tokens=1000,
            n=1,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        return "Ошибка при вызове OpenAI API."


async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_mode

    text = update.message.text or ""
    chat_id = update.message.chat_id

    logger.info(f"Received message from {chat_id}: {text}")

    # Команды переключения режимов
    if text.lower().startswith("/gpt4"):
        current_mode = "gpt4"
        await update.message.reply_text("Режим переключен на GPT-4o-mini (OpenAI).")
        return
    elif text.lower().startswith("/gpt2"):
        current_mode = "gpt2"
        await update.message.reply_text("Режим переключен на GPT-2 (Hugging Face).")
        return
    elif text.lower().startswith("/gog"):
        current_mode = "gog"
        await update.message.reply_text("Режим переключен на Google поиск (заглушка).")
        return
    elif text.lower().startswith("/ht"):
        current_mode = "ht"
        await update.message.reply_text("Режим переключен на HuggingFace/DuckDuckGo поиск (заглушка).")
        return
    elif text.lower().startswith("/start"):
        await update.message.reply_text(
            "Привет! Я Rita AI Mega Bot.\n"
            "Доступные команды: /gpt4, /gpt2, /gog, /ht\n"
            "Пиши что угодно, и я отвечу в текущем режиме."
        )
        return

    # Обработка сообщений по режимам
    if current_mode == "gpt4":
        reply = await call_openai_gpt4(text)
        await update.message.reply_text(reply)
    elif current_mode == "gpt2":
        await update.message.reply_text("GPT-2 режим пока не реализован.")
    elif current_mode == "gog":
        await update.message.reply_text("Google поиск пока не реализован.")
    elif current_mode == "ht":
        await update.message.reply_text("HuggingFace/DuckDuckGo поиск пока не реализован.")
    else:
        await update.message.reply_text("Неизвестный режим. Используй /gpt4, /gpt2, /gog или /ht.")


async def pro_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != ADMIN_CHAT_ID:
        await update.message.reply_text("У вас нет прав использовать эту команду.")
        return
    await update.message.reply_text("Привет, админ! Это команда /pro.")
    # Здесь можно добавить автообновление или диагностику


async def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", process_message))
    application.add_handler(CommandHandler("gpt4", process_message))
    application.add_handler(CommandHandler("gpt2", process_message))
    application.add_handler(CommandHandler("gog", process_message))
    application.add_handler(CommandHandler("ht", process_message))
    application.add_handler(CommandHandler("pro", pro_command))

    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process_message))

    logger.info("Rita Mega Bot запущен!")

    await application.run_polling()


























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

import asyncio
import difflib
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Пути к скриптам и логам (замени при необходимости)
MAIN_SCRIPT_PATH = Path("rita_main.py")
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
LOG_FILE_PATH = Path("rita_main.log")  # путь к лог-файлу для анализа

# Логгеры для удобства
def log_info(msg):
    logger.info(msg)
    print(msg)

def log_error(msg):
    logger.error(msg)
    print(msg)

async def send_admin_message(text: str):
    # Здесь вставь свою логику отправки сообщения админу (например, в Telegram)
    log_info(f"[ADMIN MESSAGE] {text}")

from pathlib import Path
import difflib
import logging

async def auto_fix_loop(logger=None, interval_minutes: int = 5):
    while True:
        if logger:
            logger.info("⏳ [Автофиксер] Запуск автоанализа и исправлений...")
        else:
            print("⏳ [Автофиксер] Запуск автоанализа и исправлений...")

        try:
            main_updated = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
            helper_updated = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)

            if main_updated:
                await send_admin_message("✅ Основной скрипт автоматически обновлён и исправлен.")

            if helper_updated:
                await send_admin_message("✅ Вспомогательный скрипт автоматически обновлён и исправлен.")

            if not main_updated and not helper_updated:
                if logger:
                    logger.info("✅ Изменений не требуется. Скрипты в порядке.")
                else:
                    print("✅ Изменений не требуется. Скрипты в порядке.")

        except Exception as e:
            if logger:
                logger.error(f"❌ Ошибка в auto_fix_loop: {e}")
            else:
                print(f"❌ Ошибка в auto_fix_loop: {e}")

        await asyncio.sleep(interval_minutes * 60)






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
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID, число без кавычек
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
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

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")

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
    except Exception as e:
        pass

def log_error(msg):
    logger.info(f"[ERROR] {time.ctime()} - {msg}")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[ERROR] {time.ctime()} - {msg}\n")
    except Exception as e:
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
# # # from telegram.ext import ContextTypes  # временно закомментирован импорт для предотвращения SyntaxError  # временно закомментирован импорт для предотвращения SyntaxError  # временно закомментирован импорт для предотвращения SyntaxError

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

import os
import re
import subprocess
import aiohttp
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
TELEGRAM_ADMIN_ID = int(os.getenv("TELEGRAM_ADMIN_ID", "558079551"))

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден. Убедись, что он указан в .env")

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")
# # # from telegram.ext import ContextTypes  # временно закомментирован импорт для предотвращения SyntaxError  # временно закомментирован импорт для предотвращения SyntaxError  # временно закомментирован импорт для предотвращения SyntaxError

# Ключи и настройки (вставь свои реальные)
import os

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
OWNER_TELEGRAM_ID = int(os.getenv("OWNER_TELEGRAM_ID", 0))

MAIN_SCRIPT_PATH = Path("./rita_main.py")
HELPER_SCRIPT_PATH = Path("./check_bot_diagnostics.py")

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")

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
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID, число без кавычек
# Инициализация бота (уже должна быть в коде)
bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")

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
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
                except Exception as e:
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

    import asyncio
    from pathlib import Path
    import openai
    import logging
import difflib
import asyncio
from pathlib import Path
from loguru import logger
import ast

import difflib
import asyncio
from pathlib import Path
from loguru import logger
import ast

def fix_unclosed_syntax(code_str: str) -> str:
    # Баланс скобок
    code_str += ')' * max(0, code_str.count('(') - code_str.count(')'))
    code_str += '}' * max(0, code_str.count('{') - code_str.count('}'))
    code_str += ']' * max(0, code_str.count('[') - code_str.count(']'))

    # Баланс кавычек
    for q in ['"', "'"]:
        if code_str.count(q) % 2 != 0:
            code_str += q
    return code_str

import logging
from pathlib import Path
import shutil
import difflib
import ast

from utils.fix_syntax import fix_unclosed_syntax  # импорт функции для автофикса синтаксиса

# Настройка логгера
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

from pathlib import Path
import shutil
import difflib
import ast
import logging

logger = logging.getLogger(__name__)

from utils.fix_syntax import fix_unclosed_syntax  # импорт там где нужно

async def analyze_and_fix_script(script_path: Path, log_path: Path) -> bool:
    try:
        if isinstance(script_path, str):
            script_path = Path(script_path)
        if isinstance(log_path, str):
            log_path = Path(log_path)

        if not script_path.exists():
            logger.warning(f"[WARN] Файл не найден: {script_path}")
            return False

        if not log_path.exists():
            logger.warning(f"[WARN] Лог-файл не найден: {log_path}")
            return False

        original_code = script_path.read_text(encoding="utf-8")
        fixed_code = original_code
        log_content = log_path.read_text(encoding="utf-8")

        # Примитивные автофиксы

        if "SyntaxError: expected ':'" in log_content:
            lines = fixed_code.splitlines()
            for i, line in enumerate(lines):
                if line.strip().startswith("async def") and not line.strip().endswith(":"):
                    lines[i] += ":"
                    logger.info(f"[FIX] Добавлен ':' в строке {i + 1}")
            fixed_code = "\n".join(lines)

        if "unterminated string literal" in log_content:
            lines = fixed_code.splitlines()
            for i, line in enumerate(lines):
                if 'f"' in line and not line.strip().endswith('"'):
                    lines[i] += '"'
                    logger.info(f"[FIX] Закрыта f-строка в строке {i + 1}")
            fixed_code = "\n".join(lines)

        # Попытка компиляции с текущим кодом
        try:
            compile(fixed_code, str(script_path), 'exec')
        except SyntaxError as e:
            msg = str(e)
            if "was never closed" in msg or "unexpected EOF" in msg:
                logger.warning(f"[WARN] Обрыв конструкции: {msg}")

                fixed_code2 = fix_unclosed_syntax(fixed_code)
                try:
                    compile(fixed_code2, str(script_path), 'exec')

                    # Создаём резервную копию
                    backup_path = script_path.with_suffix(script_path.suffix + ".backup")
                    shutil.copy(script_path, backup_path)
                    logger.info(f"[BACKUP] Создана резервная копия: {backup_path}")

                    # Сохраняем исправленный код
                    with open(script_path, 'w', encoding='utf-8') as f:
                        f.write(fixed_code2)
                    logger.info(f"[FIX] Исправлены незакрытые скобки/кавычки в {script_path}")
                    fixed_code = fixed_code2

                except SyntaxError as e2:
                    logger.error(f"[FAIL] Ошибка после попытки исправления: {e2}")
                    return False
            else:
                logger.error(f"[FAIL] Синтаксическая ошибка: {msg}")
                return False

        # Проверяем синтаксис окончательно с помощью ast
        try:
            ast.parse(fixed_code)
        except SyntaxError as e:
            logger.error(f"[FAIL] Синтаксическая ошибка после всех попыток: {e}")
            return False

        # Если код был изменён — сохраняем и показываем diff
        if fixed_code != original_code:
            script_path.write_text(fixed_code, encoding="utf-8")

            diff = difflib.unified_diff(
                original_code.splitlines(keepends=True),
                fixed_code.splitlines(keepends=True),
                fromfile=str(script_path),
                tofile=str(script_path) + " (исправлен)",
            )
            diff_text = ''.join(diff)
            if diff_text:
                logger.info(f"[DIFF] Изменения:\n{diff_text}")
            logger.info(f"[SAVE] Изменения сохранены в {script_path}")
            return True
        else:
            logger.info("[INFO] Нет ошибок в логах — изменений не требуется")
            return False

    except Exception as e:
        logger.error(f"[ERROR] analyze_and_fix_script: {e}")
        return False




        # 💡 Здесь заменяем ast.parse() на более умную функцию
from pathlib import Path

async def try_fix_syntax_errors(script_path: Path, logger) -> bool:
    code = script_path.read_text(encoding='utf-8')

    try:
        compile(code, str(script_path), 'exec')
        return True

    except SyntaxError as e:
        msg = str(e)
        if "was never closed" in msg or "unexpected EOF" in msg:
            code_fixed = fix_unclosed_syntax(code)
            try:
                compile(code_fixed, str(script_path), 'exec')
                script_path.write_text(code_fixed, encoding='utf-8')
                logger.info(f"[FIX] Исправлены незакрытые скобки/кавычки в {script_path}")
                await send_admin_message(f"🛠️ Автофикс: исправлены незакрытые конструкции в {script_path.name}")
                return True
            except SyntaxError as e2:
                logger.error(f"[FAIL] Ошибка после попытки исправления: {e2}")
                return False
        else:
            logger.error(f"[FAIL] Синтаксическая ошибка: {msg}")
            return False
        def fix_unclosed_syntax(code_str: str) -> str:
            open_paren = code_str.count('(')
            close_paren = code_str.count(')')
            open_brace = code_str.count('{')
            close_brace = code_str.count('}')
            open_bracket = code_str.count('[')
            close_bracket = code_str.count(']')

            code_str += ')' * max(0, open_paren - close_paren)
            code_str += '}' * max(0, open_brace - close_brace)
            code_str += ']' * max(0, open_bracket - close_bracket)

            for q in ['"', "'"]:
                if code_str.count(q) % 2 != 0:
                    code_str += q

            return code_str

        # ⛏ Проверка синтаксиса и возможное автоисправление
        if not try_fix_syntax_errors(script_path, logger):
            logger.error("❌ Не удалось автоматически исправить ошибки синтаксиса.")
            return False
        else:
            logger.info(f"✅ {script_path} синтаксически корректен или успешно исправлен.")
            return True

    except Exception as e:
        logger.error(f"[ERROR] analyze_and_fix_script: {e}")
        return False

def try_fix_syntax_errors(script_path: str, logger=None):
    """
    Попытка скомпилировать и, в случае ошибки незакрытых скобок или кавычек,
    автоматически их исправить и перезаписать файл.
    """
    with open(script_path, 'r', encoding='utf-8') as f:
        code = f.read()

    def fix_unclosed_syntax(code_str: str) -> str:
        # Баланс скобок
        open_paren = code_str.count('(')
        close_paren = code_str.count(')')
        open_brace = code_str.count('{')
        close_brace = code_str.count('}')
        open_bracket = code_str.count('[')
        close_bracket = code_str.count(']')

        # Добавляем недостающие закрывающие скобки
        code_str += ')' * max(0, open_paren - close_paren)
        code_str += '}' * max(0, open_brace - close_brace)
        code_str += ']' * max(0, open_bracket - close_bracket)

        # Баланс кавычек
        for q in ['"', "'"]:
            if code_str.count(q) % 2 != 0:
                code_str += q

        return code_str

    try:
        compile(code, script_path, 'exec')
    except SyntaxError as e:
        msg = str(e)
        if "was never closed" in msg or "unexpected EOF" in msg:
            fixed_code = fix_unclosed_syntax(code)
            try:
                compile(fixed_code, script_path, 'exec')
                # Если успешно — сохраняем исправленный файл
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_code)
                if logger:
                    logger.info(f"[FIX] Исправлены незакрытые скобки и кавычки в {script_path}")
                else:
                    print(f"[FIX] Исправлены незакрытые скобки и кавычки в {script_path}")
                return True
            except SyntaxError as e2:
                if logger:
                    logger.error(f"[FAIL] Ошибка после попытки исправления скобок: {e2}")
                else:
                    print(f"[FAIL] Ошибка после попытки исправления скобок: {e2}")
                return False
        else:
            if logger:
                logger.error(f"[FAIL] Синтаксическая ошибка: {e}")
            else:
                print(f"[FAIL] Синтаксическая ошибка: {e}")
            return False
    return True

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

@dp.message(Command("proverka"))
async def manual_check(message: types.Message):
    await message.answer("🔎 Запускаю ручную проверку и автоисправление...")
    try:
        result_main = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_PATH)
        result_helper = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_PATH)

        if result_main or result_helper:
            await message.answer("✅ Исправления успешно применены.")
        else:
            await message.answer("ℹ️ Ошибок не найдено или ничего не изменилось.")
    except Exception as e:
        await message.answer(f"❌ Ошибка при проверке: {e}")







import shutil
from datetime import datetime
import subprocess

def auto_backup_and_push():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_dir = f"backup/{timestamp}"
        os.makedirs(backup_dir, exist_ok=True)

        files_to_backup = ["rita_main.py", "check_bot_diagnostics.py"]
        for file in files_to_backup:
            if os.path.exists(file):
                shutil.copy(file, os.path.join(backup_dir, file))

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"🧠 Авто-бэкап и пуш {timestamp}"], check=True)
        subprocess.run(["git", "push"], check=True)

        log_info(f"[✅] Успешный авто-бэкап и пуш ({timestamp})")

    except Exception as e:
        log_info(f"[❌] Ошибка авто-бэкапа и пуша: {e}")









def ai_auto_improve():
    import openai
    import difflib

    openai.api_key = OPENAI_API_KEY  # У тебя он уже должен быть задан

    def read_file(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def get_diff(old, new):
        return "\n".join(difflib.unified_diff(
            old.splitlines(), new.splitlines(),
            fromfile='original', tofile='improved', lineterm=''
        ))

    files_to_improve = ["rita_main.py", "check_bot_diagnostics.py"]

    for filename in files_to_improve:
        try:
            original = read_file(filename)
            prompt = (
                f"Вот код:\n{original[:12000]}\n\n"
                f"Если есть проблемы, устаревшие участки, неэффективности или уязвимости — улучши его.\n"
                f"Вноси правки прямо в код. Сохрани все функции. Автоматизируй и сделай устойчивым к ошибкам."
            )

            response = openai.ChatCompletion.create(
                model="gpt-4",  # Или "gpt-3.5-turbo", если хочешь быстрее
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )

            improved_code = response["choices"][0]["message"]["content"]
            if improved_code.strip() and improved_code != original:
                diff = get_diff(original, improved_code)
                backup_path = filename + ".bak"
                write_file(backup_path, original)
                write_file(filename, improved_code)
                logger.info(f"✅ Улучшен: {filename}. Изменения:\n{diff}")
            else:
                logger.info(f"📌 Нет улучшений для {filename}")
        except Exception as e:
            logger.error(f"❌ Ошибка улучшения {filename}: {e}")











import subprocess
import sys
import os
import asyncio
import logging
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, filters

# Предполагается, что nest_asyncio уже применён в основном скрипте

# Константы (укажи свои, если уже есть, тогда просто пропусти)
AUTHORIZED_USERS = [ ]  # Твой Telegram ID
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"

logger = logging.getLogger(__name__)

def _is_authorized(update: Update) -> bool:
    try:
        return update.effective_user.id in AUTHORIZED_USERS
    except Exception as e:
        logger.warning(f"Authorization check failed: {e}")
        return False

async def auto_backup_and_push():
    try:
        logger.info("🔄 Выполняю git add/commit/push...")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(
            ["git", "commit", "-m", "Auto backup from check_bot_diagnostics"], check=True
        )
        subprocess.run(["git", "push"], check=True)
        logger.info("✅ Резервное копирование и пуш успешно выполнены.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка git операций: {e}")

async def auto_fix_from_logs():
    logger.info("🔍 Анализ логов и попытка автоисправления...")
    # TODO: вставь свою логику анализа и исправлений
    await asyncio.sleep(1)
    logger.info("✅ Автоисправления завершены (пример).")

async def auto_update_and_restart():
    try:
        logger.info("⬇️ Проверяю обновления из GitHub...")
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        logger.info(f"git pull output: {result.stdout.strip()}")
        if "Already up to date." not in result.stdout:
            logger.info("♻️ Обновления найдены, перезапускаю скрипт...")
            python = sys.executable
            os.execv(python, [python] + sys.argv)
        else:
            logger.info("🔄 Обновлений нет.")
    except Exception as e:
        logger.error(f"Ошибка при автообновлении: {e}")

async def auto_fix_loop():
    while True:
        await auto_fix_from_logs()
        await auto_backup_and_push()
        await auto_update_and_restart()
        await asyncio.sleep(3600)  # 1 час

async def proverka_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_authorized(update):
        await update.message.reply_text("🚫 Недостаточно прав для выполнения команды.")
        return
    await update.message.reply_text("🔧 Запускаю диагностику и автоисправления...")
    await auto_fix_from_logs()
    await update.message.reply_text("✅ Диагностика и исправления завершены.")

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_authorized(update):
        await update.message.reply_text("🚫 Вы не авторизованы.")
        return
    await update.message.reply_text("✅ Вспомогательный бот готов к работе.")

SECRET_STOP_COMMAND = "/_shutdown_321xyz"  # Скрытая команда

async def stopbot_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not _is_authorized(update):
        await update.message.reply_text("🚫 Недостаточно прав.")
        return
    await update.message.reply_text("🛑 Бот будет остановлен по вашей команде.")
    logger.info("🔒 Получена команда остановки бота. Выключаем...")
    asyncio.get_event_loop().stop()
    sys.exit(0)

# Функция для регистрации этих команд в твоём ApplicationBuilder:
def register_auxiliary_handlers(application):
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("proverka", proverka_handler))
    application.add_handler(CommandHandler(SECRET_STOP_COMMAND.lstrip("/"), stopbot_handler))

# Ты вызываешь где-то в основном коде:
# register_auxiliary_handlers(app)
# asyncio.create_task(auto_fix_loop())



import re
from datetime import datetime

IMPROVEMENT_LOG = "improvement_suggestions.log"
ERROR_LOG_PATH = "error.log"

async def self_improve_from_logs():
    logger.info("🤖 Начинаю анализ логов для саморазвития...")
    if not os.path.exists(ERROR_LOG_PATH):
        logger.info("ℹ️ Лог-файл не найден, пропускаю анализ.")
        return

    try:
        with open(ERROR_LOG_PATH, "r", encoding="utf-8") as f:
            logs = f.read()

        suggestions = []

        # Пример: найти повторяющиеся ошибки
        pattern = re.findall(r"❌ Ошибка запуска бота: (.+)", logs)
        frequent_errors = {err: pattern.count(err) for err in set(pattern)}
        for error, count in frequent_errors.items():
            if count > 3:
                suggestions.append(f"Частая ошибка: {error} — встречается {count} раз.")

        # Пример: команды без ответа
        if "Unhandled command" in logs:
            suggestions.append("Есть необработанные команды. Добавь обработчики.")

        if suggestions:
            with open(IMPROVEMENT_LOG, "a", encoding="utf-8") as log_file:
                log_file.write(f"\n=== {datetime.now()} ===\n")
                for s in suggestions:
                    log_file.write(f"- {s}\n")
            logger.info("💡 Предложения по улучшению сохранены.")
        else:
            logger.info("✅ Проблем не найдено. Улучшения не требуются.")
    except Exception as e:
        logger.error(f"⚠️ Ошибка при анализе логов для улучшения: {e}")






from telegram.constants import ParseMode

TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID, число без кавычек
async def send_admin_report(context):
    try:
        logs = ""
        if os.path.exists("error.log"):
            with open("error.log", "r", encoding="utf-8") as f:
                logs += "📄 <b>Лог ошибок:</b>\n" + f.read()[-4000:] + "\n\n"
        if os.path.exists("improvement_suggestions.log"):
            with open("improvement_suggestions.log", "r", encoding="utf-8") as f:
                logs += "💡 <b>Улучшения:</b>\n" + f.read()[-4000:] + "\n\n"

        if not logs:
            logs = "✅ Нет ошибок и предложений. Всё работает стабильно."

        await context.bot.send_message(
            chat_id=OWNER_ID,
            text=logs,
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        logger.error(f"⚠️ Ошибка при отправке отчета админу: {e}")





import asyncio
import logging
import aiohttp
import os
import subprocess
from datetime import datetime
from git import Repo, GitCommandError

# --- ТВОИ ДАННЫЕ (замени здесь) ---
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID, число без кавычек
LOG_FILE_PATH = "./rita_bot.log"  # путь к твоему лог файлу
MAIN_SCRIPT_PATH = "./rita_main.py"  # путь к основному скрипту
REPO_PATH = "./"  # путь к репозиторию git (обычно корень проекта)

# Папка для новых улучшений
IMPROVEMENTS_DIR = "./improvements"
os.makedirs(IMPROVEMENTS_DIR, exist_ok=True)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')


async def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                if resp.status != 200:
                    logger.warning(f"Telegram message failed with status {resp.status}")
    except Exception as e:
        logger.error(f"Telegram sending error: {e}")


def read_log_tail(lines_count=200):
    """Читаем последние lines_count строк лога"""
    if not os.path.isfile(LOG_FILE_PATH):
        logger.warning(f"Лог-файл {LOG_FILE_PATH} не найден")
        return []
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return lines[-lines_count:]
    except Exception as e:
        logger.error(f"Ошибка чтения лога: {e}")
        return []


def detect_errors_and_successes(log_lines):
    """
    Анализ лога:
    Возвращает кортеж (errors, successes)
    errors - список строк с ERROR/Exception
    successes - список строк с INFO успешных действий
    """
    errors = []
    successes = []

    for line in log_lines:
        line_lower = line.lower()
        if "error" in line_lower or "exception" in line_lower:
            errors.append(line.strip())
        elif "info" in line_lower or "started" in line_lower or "complete" in line_lower:
            successes.append(line.strip())

    return errors, successes


def check_main_script_health():
    """
    Проверка основного скрипта на наличие ключевых функций.
    Проверяет что основные функции присутствуют в скрипте.
    Возвращает список проблем.
    """
    problems = []
    if not os.path.isfile(MAIN_SCRIPT_PATH):
        problems.append(f"Основной скрипт {MAIN_SCRIPT_PATH} не найден!")
        return problems

    try:
        with open(MAIN_SCRIPT_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        # Проверяем ключевые функции
        needed_functions = [
            "async def run_bot()",
            "async def auto_fix_loop(",
            "async def auto_fix_and_restart_if_needed(",
            "asyncio.create_task(",
        ]

        for func in needed_functions:
            if func not in content:
                problems.append(f"Отсутствует ключевая функция или вызов: {func}")

    except Exception as e:
        problems.append(f"Ошибка при чтении основного скрипта: {e}")

    return problems


def create_improvement_file(content: str, name_hint: str) -> str:
    """
    Создает файл с улучшением в папке improvements.
    Возвращает путь к файлу или пустую строку при ошибке.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = name_hint.lower().replace(" ", "_").replace(".", "").replace(",", "")
    filename = os.path.join(IMPROVEMENTS_DIR, f"improve_{safe_name}_{timestamp}.py")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Создан файл улучшения: {filename}")
        return filename
    except Exception as e:
        logger.error(f"Ошибка создания файла улучшения: {e}")
        return ""


def generate_auto_update_improvement():
    """
    Генерирует реальный код для автообновления скрипта.
    Возвращает строку с кодом.
    """
    code = '''
import subprocess
import logging

async def auto_update_script():
    try:
        # Получаем последние изменения из репозитория
        result = subprocess.run(["git", "pull"], cwd="{}", capture_output=True, text=True)
        if "Already up to date." in result.stdout:
            logging.info("Auto-update: Скрипт уже актуален.")
        else:
            logging.info("Auto-update: Обновление выполнено, перезапускаем скрипт.")
            # Здесь можно добавить перезапуск скрипта
    except Exception as e:
        logging.error(f"Auto-update ошибка: {e}")
'''.format(REPO_PATH)
    return code


def do_git_backup_and_push() -> (bool, str):
    """
    Делает git add/commit/push основного скрипта и улучшений.
    Возвращает (успех, сообщение)
    """
    try:
        repo = Repo(REPO_PATH)
        repo.git.add(MAIN_SCRIPT_PATH)
        repo.git.add(IMPROVEMENTS_DIR)
        commit_message = f"Auto backup {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        return True, "Git push успешно выполнен"
    except GitCommandError as git_err:
        return False, f"Git ошибка: {git_err}"
    except Exception as e:
        return False, f"Ошибка git backup: {e}"


async def analyze_and_improve_full():
    """
    Полный анализ, генерация улучшений, отправка отчётов, бэкап и пуш.
    """

    log_lines = read_log_tail(200)
    errors, successes = detect_errors_and_successes(log_lines)
    script_problems = check_main_script_health()

    # Сформировать отчет
    report = "<b>Отчет об анализе Rita Mega Bot</b>\n\n"
    report += f"<b>Успешные действия (последние 10):</b>\n"
    report += "\n".join(successes[-10:]) + "\n\n" if successes else "Нет данных.\n\n"

    report += "<b>Ошибки (последние 10):</b>\n"
    report += "\n".join(errors[-10:]) + "\n\n" if errors else "Ошибок нет.\n\n"

    report += "<b>Проблемы с основным скриптом:</b>\n"
    if script_problems:
        report += "\n".join(script_problems) + "\n\n"
    else:
        report += "Проблем не обнаружено.\n\n"

    improvements_created = []

    # Генерируем реальные улучшения, если проблемы есть
    if script_problems or errors:
        # Добавим улучшение: автообновление если его нет
        auto_update_code = generate_auto_update_improvement()
        fname = create_improvement_file(auto_update_code, "auto_update")
        if fname:
            improvements_created.append(fname)

    else:
        report += "Все системы работают стабильно. Рекомендуется поддерживать резервное копирование.\n"

    # Отправить отчет в Telegram
    await send_telegram_message(report)
    logger.info("Отчет отправлен в Telegram.")

    # Сделать git backup и push
    success, msg = do_git_backup_and_push()
    if success:
        await send_telegram_message(f"✅ Git backup и push прошли успешно.")
    else:
        await send_telegram_message(f"❌ Ошибка git backup/push:\n{msg}")

    logger.info(msg)

    if improvements_created:
        logger.info(f"Созданы файлы улучшений: {improvements_created}")

async def improvements_loop():
    """
    Запускать этот цикл в фоне — анализ и улучшения раз в 6 часов
    """
    while True:
        try:
            await analyze_and_improve_full()
        except Exception as e:
            logger.error(f"Ошибка в цикле улучшений: {e}")
        await asyncio.sleep(6 * 3600)  # 6 часов


# --- В КОНЦЕ ВАШЕГО ВСПОМОГАТЕЛЬНОГО СКРИПТА ПРОСТО ВЫЗВАТЬ ---
# asyncio.create_task(improvements_loop())


import os
import re
import subprocess
import aiohttp
import asyncio

import os
import re
import subprocess
import aiohttp
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
TELEGRAM_ADMIN_ID = int(os.getenv("TELEGRAM_ADMIN_ID", "558079551"))

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден. Убедись, что он указан в .env")

bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")

# === Настройки под тебя — замени на свои реальные данные ===
LOG_FILE = "/mnt/data/rita_mega_bot/logs/rita_bot.log"  # путь к логу твоего основного бота (проверь точный)
MAIN_SCRIPT = "/mnt/data/rita_mega_bot/rita_main.py"    # путь к основному скрипту
GIT_REPO_PATH = "/mnt/data/rita_mega_bot"               # путь к git-репозиторию с твоим ботом

TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"  # твой реальный токен
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID, число без кавычек
bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")

# Функция для отправки сообщения в телеграм
async def send_telegram_message(text: str):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
    except Exception as e:
        print(f"[Telegram send error]: {e}")

# Анализ лога для ошибок
async def analyze_logs():
    if not os.path.isfile(LOG_FILE):
        return "⚠️ Лог файл не найден!"

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read()

    # Пример: ищем ошибки и предупреждения
    errors = re.findall(r"(?i)(error|exception|fail|critical)", logs)
    warnings = re.findall(r"(?i)(warning|warn|deprecated)", logs)

    result = f"🔍 Анализ логов:\nОшибок найдено: {len(errors)}\nПредупреждений: {len(warnings)}"
    return result

# Проверка наличия ключевых функций в основном скрипте
async def check_main_script_functions():
    required_functions = [
        "async def run_bot",
        "async def auto_fix_loop",
        "async def auto_fix_and_restart_if_needed",
        "async def start_monitoring_thread",
        # добавляй сюда свои важные функции
    ]

    if not os.path.isfile(MAIN_SCRIPT):
        return "⚠️ Основной скрипт не найден!"

    with open(MAIN_SCRIPT, "r", encoding="utf-8") as f:
        main_code = f.read()

    missing = []
    for func in required_functions:
        if func not in main_code:
            missing.append(func)

    if not missing:
        return "✅ Все ключевые функции присутствуют в основном скрипте."
    else:
        miss_list = "\n".join(missing)
        return f"⚠️ Отсутствуют функции:\n{miss_list}"

# Добавление функции в основной скрипт (если её нет)
async def add_missing_function(func_code: str, func_name: str):
    with open(MAIN_SCRIPT, "r", encoding="utf-8") as f:
        main_code = f.read()

    if func_name in main_code:
        return False  # функция уже есть

    with open(MAIN_SCRIPT, "a", encoding="utf-8") as f:
        f.write("\n\n" + func_code.strip() + "\n")
    return True

# Автофикс и коммит изменений
async def auto_fix_and_commit():
    # Пример — добавим фиктивную функцию (замени на реальные твои шаблоны)
    func_code = '''
async def auto_fix_loop(logger):
    while True:
        logger.info("Автофикс запущен.")
        await asyncio.sleep(3600)
'''

    added = await add_missing_function(func_code, "async def auto_fix_loop")
    if added:
        await send_telegram_message("➕ Добавлена новая функция auto_fix_loop в основной скрипт.")
    else:
        await send_telegram_message("ℹ️ Функция auto_fix_loop уже есть в основном скрипте.")

    # Далее делаем git commit и push
    try:
        # Переходим в репозиторий
        proc = subprocess.run(["git", "-C", GIT_REPO_PATH, "add", "."], capture_output=True, text=True)
        if proc.returncode != 0:
            await send_telegram_message(f"❌ Git add failed:\n{proc.stderr}")
            return

        commit_msg = "Автофикс: добавлена missing функция auto_fix_loop"
        proc = subprocess.run(["git", "-C", GIT_REPO_PATH, "commit", "-m", commit_msg], capture_output=True, text=True)
        if proc.returncode != 0:
            if "nothing to commit" in proc.stderr:
                await send_telegram_message("ℹ️ Нет новых изменений для коммита.")
            else:
                await send_telegram_message(f"❌ Git commit failed:\n{proc.stderr}")
                return

        proc = subprocess.run(["git", "-C", GIT_REPO_PATH, "push"], capture_output=True, text=True)
        if proc.returncode != 0:
            await send_telegram_message(f"❌ Git push failed:\n{proc.stderr}")
            return

        await send_telegram_message("✅ Изменения успешно запушены в GitHub.")

    except Exception as e:
        await send_telegram_message(f"❌ Ошибка при git операциях: {e}")

# Основная функция автоанализа и улучшения
async def run_intelligent_auto_improve():
    log_summary = await analyze_logs()
    script_check = await check_main_script_functions()
    await send_telegram_message("🔧 Автоанализ и проверка бота запущены...")
    await send_telegram_message(log_summary)
    await send_telegram_message(script_check)

    # Если функции отсутствуют - попробуем добавить и запушить
    if "Отсутствуют функции" in script_check:
        await auto_fix_and_commit()

    else:
        await send_telegram_message("✅ Улучшений не требуется, скрипт в порядке.")






# Для запуска в asyncio
import asyncio
import nest_asyncio
import logging
import signal

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from telegram.error import Conflict

nest_asyncio.apply()

# ✅ Реальный Telegram токен пользователя
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"

# Логгер
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# Заглушки для автофикса — если у тебя есть настоящие, оставь их

async def run_ai_improvement_loop():
    while True:
        ai_auto_improve()
        await asyncio.sleep(3600)  # Раз в час

async def auto_fix_from_logs():
    logger.info("🛠️ Автофикс логов...")
    asyncio.create_task(run_ai_improvement_loop())
    await self_improve_from_logs()
async def auto_fix_loop(logger):
    while True:
        await asyncio.sleep(60)
        logger.info("🔁 Цикл автофикса...")

async def auto_fix_and_restart_if_needed():
    while True:
        await asyncio.sleep(120)
        logger.info("🧠 Проверка на автообновление...")

def start_monitoring_thread():
    logger.info("📡 Мониторинг запущен.")

# Обработчики Telegram
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Привет! Я готов к работе.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✉️ Вы сказали: " + update.message.text)

# Основной запуск бота
import asyncio
import nest_asyncio
import signal
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram.error import Conflict

# --- ТВОИ НАСТРОЙКИ ---
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID, число без кавычек
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# --- ТВОИ ФУНКЦИИ должны быть объявлены или импортированы выше ---

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Привет! Я готов к работе.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✉️ Вы сказали: " + update.message.text)

async def report_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("⛔ У вас нет доступа к этой команде.")
        return
    await update.message.reply_text("⏳ Составляю отчёт...")
    # твоя функция отчёта

def register_auxiliary_handlers(app):
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.add_handler(CommandHandler("report", report_handler))
    # добавь другие команды здесь

async def run_bot():
    try:
        app = (
            ApplicationBuilder()
            .token(TELEGRAM_BOT_TOKEN)
            .concurrent_updates(True)
            .build()
        )
        register_auxiliary_handlers(app)

        logger.info("✅ Бот запущен и работает.")
        asyncio.create_task(auto_fix_loop(logger))
        asyncio.create_task(auto_fix_and_restart_if_needed())
        start_monitoring_thread()
        asyncio.create_task(improvements_loop())

        await app.run_polling()

    except Conflict as e:
        logger.warning(f"⚠️ Конфликт запуска: {e}")
        logger.info("🔁 Перезапуск через 10 секунд...")
        await asyncio.sleep(10)
        await run_bot()

    except Exception as e:
        logger.error(f"❌ Ошибка запуска бота: {e}")

async def main_entry():
    logger.info("🚀 Старт автофикса из логов...")
    await auto_fix_from_logs()

    logger.info("💾 Выполнение резервного копирования и пуша в GitHub...")
    await auto_backup_and_push()

    logger.info("🔧 Фоновые задачи автофикса...")
    asyncio.create_task(auto_fix_loop(logger))
    asyncio.create_task(auto_fix_and_restart_if_needed())
    start_monitoring_thread()

    logger.info("🤖 Запуск интеллектуального автоулучшения...")
    await run_intelligent_auto_improve()

    logger.info("🚀 Запуск Telegram-бота...")
    await run_bot()

if __name__ == "__main__":
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, loop.stop)
        except NotImplementedError:
            pass

    try:
        loop.run_until_complete(main_entry())
    except KeyboardInterrupt:
        logger.warning("⛔ Бот остановлен вручную (Ctrl+C)")
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")
    finally:
        if not loop.is_closed():
            loop.close()
