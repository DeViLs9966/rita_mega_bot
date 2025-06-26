from telegram.ext import Application
from auto_fix_tools import run_auto_fix_analysis
import sys
import os
sys.path.append(os.getcwd())
from auto_fix_tools import run_auto_fix_analysis
from pathlib import Path
import os
import sys
import logging
import sys
import logging
import sys
sys.stdout.reconfigure(encoding='utf-8')


def safe_path_join(parent, child):
    import pathlib
    try:
        if parent is None:
            return pathlib.Path(child)
        else:
            return pathlib.Path(parent) / child
    except Exception:
        return pathlib.Path(child)
import asyncio
import sys
def run_main():
    try:
        if sys.version_info >= (3, 7):
            loop = asyncio.get_event_loop()
            if loop.is_running():
                import nest_asyncio
                nest_asyncio.apply()
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
def safe_get_parent(path):
    import pathlib
    try:
        p = pathlib.Path(path)
        return safe_get_parent(p)
    except Exception:
        return None
import asyncio
def safe_async_run(coro):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # Нет запущенного event loop
        loop = None
    if loop and loop.is_running():
        import nest_asyncio
        nest_asyncio.apply()
        return asyncio.create_task(coro)
    else:
        return asyncio.run(coro)
import sys
import traceback
def log_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Чтобы не мешать выходу через Ctrl+C
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    print("Ошибка (с трейсбеком):")
    traceback.print_exception(exc_type, exc_value, exc_traceback)
sys.excepthook = log_exceptions
import sys
import traceback


# --- Загрузка переменных окружения ---
import sys
import os
import traceback
import logging
import asyncio
from dotenv import load_dotenv
import openai

# Настройка глобальной обработки исключений — логируем полный traceback в stderr
def log_exceptions(exc_type, exc_value, exc_traceback):
    traceback.print_exception(exc_type, exc_value, exc_traceback)

sys.excepthook = log_exceptions

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# --- Загрузка переменных окружения ---
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Поддержка двух вариантов названия для ADMIN_CHAT_ID
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID") or os.getenv("ADMIN_TELEGRAM_ID")

# Проверки наличия ключей
if not TELEGRAM_BOT_TOKEN:
    logger.error("Ошибка: TELEGRAM_BOT_TOKEN не найден в .env")
    sys.exit(1)
if not OPENAI_API_KEY:
    logger.error("Ошибка: OPENAI_API_KEY не найден в .env")
    sys.exit(1)
if not HF_API_TOKEN:
    logger.error("Ошибка: HF_API_TOKEN не найден в .env")
    sys.exit(1)
if not ADMIN_CHAT_ID:
    logger.error("Ошибка: ADMIN_CHAT_ID или ADMIN_TELEGRAM_ID не найден в .env")
    sys.exit(1)

try:
    ADMIN_CHAT_ID = int(ADMIN_CHAT_ID)
except ValueError:
    logger.error("ADMIN_CHAT_ID должен быть числом!")
    sys.exit(1)

# Логирование подгруженных ключей (первые 10 символов, чтобы не раскрывать полностью)
logger.info(f"Telegram Token: {TELEGRAM_BOT_TOKEN[:10]}... (длина {len(TELEGRAM_BOT_TOKEN)})")
logger.info(f"OpenAI Key: {OPENAI_API_KEY[:10]}... (длина {len(OPENAI_API_KEY)})")
logger.info(f"HuggingFace Token: {HF_API_TOKEN[:10]}... (длина {len(HF_API_TOKEN)})")
logger.info(f"Admin Chat ID: {ADMIN_CHAT_ID}")

# Инициализация OpenAI
openai.api_key = OPENAI_API_KEY


# Пример асинхронного вызова OpenAI с исправленной моделью
async def call_openai_gpt4(prompt: str) -> str:
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",  # Обязательно используй именно эту модель!
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
# Далее — твой основной код скрипта check_bot_diagnostics.py,
# где используешь эти переменные и функцию call_openai_gpt4
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
with open('.token_clean') as f:
    cleaned_token = f.read().strip()
import traceback
# check_bot_diagnostics.py — БЛОК 1 из 6







import sys
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
handler.stream.reconfigure(encoding='utf-8')

logging.basicConfig(level=logging.INFO)
logging.getLogger().addHandler(handler)












TOKEN_FILE = Path(".token_clean")
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
load_dotenv()  # Загружает переменные из .env в окружение
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
GITHUB_PAT = os.getenv("GITHUB_PAT")
import sys
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID") or os.getenv("ADMIN_TELEGRAM_ID")
if ADMIN_CHAT_ID is None:
    print("Ошибка: переменная ADMIN_CHAT_ID или ADMIN_TELEGRAM_ID не установлена в окружении")
    sys.exit(1)
try:
    ADMIN_CHAT_ID = int(ADMIN_CHAT_ID)
except ValueError:
    print("Ошибка: ADMIN_CHAT_ID должен быть числом")
    sys.exit(1)
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
LOG_FILE = Path("safe_path_join(logs, rita_bot).log")
MAIN_SCRIPT = Path("/safe_path_join(mnt, data)/safe_path_join(rita_mega_bot, rita_main).py")
GIT_REPO_PATH = Path("/safe_path_join(mnt, data)/rita_mega_bot")
from dotenv import load_dotenv
load_dotenv(dotenv_path="/safe_path_join(data, data)/safe_path_join(com.termux, files)/safe_path_join(home, rita_mega_bot)/.env")
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
from dotenv import load_dotenv
load_dotenv()  # Загружаем переменные из .env
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
print(f"[DEBUG] TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN!r}")  # отладочный вывод
import asyncio
# другие нужные импорты
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from utils.fix_syntax import fix_unclosed_syntax, try_fix_syntax
import datetime
import aiohttp
import asyncio
import openai
import requests
import difflib
import datetime
import sys
import time
import json
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
import requests
import hashlib
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
import sys
import psutil
from telegram.error import Conflict
os.environ['TZ'] = 'UTC'  # Устанавливаем переменную окружения TZ в UTC
import pytz  # Импортируем pytz, чтобы APScheduler не ругался на таймзону
level=logging.DEBUG,
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
logging.basicConfig(level=logging.INFO)
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
@dp.message(Command("proverka"))
async def proverka_handler(message: types.Message):
    await message.reply("Бот работает, safe_path_join(команда, proverka) получена!")
import asyncio

def read_logs():
    try:
        # Получаем путь к логу, вызывая функцию safe_path_join с нужными аргументами
        log_path = safe_path_join(logs, "rita_bot.log")  # если имя файла - rita_bot.log

        with open(log_path, "r", encoding="utf-8") as f:
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
import sys
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

import os
import sys
import logging
from telegram import Bot
import openai

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
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

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
        url = f"https://safe_path_join(api.telegram.org, bot){TELEGRAM_BOT_TOKEN}/sendMessage"
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
        current_mode = Path("gpt4")
        await update.message.reply_text("Режим переключен на GPT-4o-mini (OpenAI GPT-4).")
        return
    elif text.lower().startswith("/gpt2"):
        current_mode = Path("gpt2")
        await update.message.reply_text("Режим переключен на GPT-2 (HuggingFace GPT-2).")
        return
    elif text.lower().startswith("/gog"):
        current_mode = Path("gog")
        await update.message.reply_text("Режим переключен на Google поиск.")
        return
    elif text.lower().startswith("/ht"):
        current_mode = Path("ht")
        await update.message.reply_text("Режим переключен на safe_path_join(HuggingFace, DuckDuckGo) поиск.")
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
        await update.message.reply_text("safe_path_join(HuggingFace, DuckDuckGo) поиск пока не реализован.")
    else:
        await update.message.reply_text("Неизвестный режим. safe_path_join(Используй, gpt4), /gpt2, /gog safe_path_join(или, ht).")
async def pro_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != ADMIN_CHAT_ID:
        await update.message.reply_text("У вас нет прав использовать эту команду.")
        return
    await update.message.reply_text("Привет, админ! Это safe_path_join(команда, pro).")
    # Здесь можно добавить автообновление или диагностику
async def main():
    application = Application.builder().token(TELEGRAM_TOKEN).close_loop(False).build()
    asyncio.create_task(background_auto_fix_loop())
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
import logging

logger = logging.getLogger(__name__)

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
        logger.info("[❌] Завершение работы по Ctrl+C или команде завершения.")
    except RuntimeError as e:
        if "Cannot close a running event loop" in str(e):
            logger.info("[⚠️] Event loop уже запущен. Работа продолжается.")
        else:
            raise
'''

        if 'if __name__ == "__main__"' not in content:
            logger.warning(f"[WARN] Блок запуска не найден в {filepath}, ничего не изменено.")
            return

        # Заменяем существующий блок запуска целиком
        content_new = re.sub(
            r'if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:\s*(?:\n[ \t]+.+)+',
            fixed_block.strip(),
            content,
            flags=re.MULTILINE
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content_new)

        logger.info(f"[INFO] Блок запуска в {filepath} успешно обновлён.")
    except Exception as e:
        logger.error(f"[ERROR] Ошибка при исправлении {filepath}: {e}")


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
LOG_FILE_PATH = Path("safe_path_join(logs, rita_bot).log")
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
async def auto_fix_from_logs():
    log_info("[INFO] Запуск автоанализа логов...")
    try:
        # Обязательно оборачиваем в Path, чтобы избежать ошибок 'str' object has no attribute 'exists'


        rita_main_path = Path("rita_main.py")
        rita_log_path = Path("logs/rita_bot.log")           # заменили на правильный путь
        check_bot_path = Path("check_bot_diagnostics.py")
        check_log_path = Path("logs/rita_bot.log")          # также заменили

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
        url = f"https://safe_path_join(api.telegram.org, bot){BOT_TOKEN}/sendMessage"
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
# Пути к скриптам и логам (замени при необходимости)
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
LOG_FILE_PATH = Path("safe_path_join(logs, rita_bot).log")  # путь к лог-файлу для анализа
# Логгеры для удобства
def log_info(msg):
    logger.info(msg)
    print(msg)
def log_error(msg):
    logger.error(msg)
    print(msg)
import difflib
async def auto_fix_loop(logger=None, interval_minutes: int = 5):
    while True:
        if logger:
            logger.info("⏳ [Автофиксер] Запуск автоанализа и исправлений...")
        else:
            print("⏳ [Автофиксер] Запуск автоанализа и исправлений...")
        try:
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
import sys
import subprocess
import time
# Пути к скриптам и логу (замени на свои пути, если надо)
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
LOG_FILE_PATH = Path("safe_path_join(logs, rita_bot).log")
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

import psutil
import asyncio
import logging

logger = logging.getLogger(__name__)

def log_info(msg):
    logger.info(msg)

def log_error(msg):
    logger.error(msg)

def kill_processes_by_script_name(script_name: str):
    """
    Завершает все процессы python, в которых в командной строке есть script_name.
    """
    try:
        for proc in psutil.process_iter(['pid', 'cmdline']):
            cmdline = proc.info['cmdline']
            if cmdline and script_name in " ".join(cmdline):
                log_info(f"Завершаем процесс PID {proc.pid} для {script_name}")
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except psutil.TimeoutExpired:
                    proc.kill()
    except Exception as e:
        log_error(f"Ошибка при завершении процессов {script_name}: {e}")

def fix_rita_main_asyncio_run():
    """
    Исправляет в rita_main.py вызов asyncio.run(main()) на явный event loop с обработкой KeyboardInterrupt.
    """
    try:
        with open("rita_main.py", "r", encoding="utf-8") as f:
            lines = f.readlines()

        changed = False
        new_lines = []
        for line in lines:
            if "asyncio.run(main())" in line:
                indent = line[:len(line) - len(line.lstrip())]  # Выделяем отступ
                new_lines.append(f"{indent}loop = asyncio.get_event_loop()\n")
                new_lines.append(f"{indent}try:\n")
                new_lines.append(f"{indent}    loop.run_until_complete(main())\n")
                new_lines.append(f"{indent}except (KeyboardInterrupt, SystemExit):\n")
                new_lines.append(f"{indent}    pass\n")
                changed = True
            else:
                new_lines.append(line)

        if changed:
            with open("rita_main.py", "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            logger.info("[INFO] ✅ rita_main.py: исправлен вызов asyncio.run(main()) на явный event loop")
        else:
            logger.info("[INFO] ⚠️ rita_main.py: asyncio.run(main()) не найден — пропущено исправление")
    except Exception as e:
        logger.error(f"[ERROR] ❌ Ошибка при замене asyncio.run: {e}")

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



import os
import threading
import subprocess
import logging
from pathlib import Path
from aiogram import Bot  # или импортируй из другого пакета, если нужно

# --- Константы и ключи ---
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
OWNER_TELEGRAM_ID = int(os.getenv("OWNER_TELEGRAM_ID", 0))

parent = Path(__file__).parent
MAIN_SCRIPT_PATH = parent / "rita_main.py"
DIAGNOSTICS_SCRIPT_PATH = parent / "check_bot_diagnostics.py"
LOG_DIR = parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "rita_bot.log"

# Настройка логгера
logging.basicConfig(
    filename=str(LOG_FILE),
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",
)
logger = logging.getLogger(__name__)

bot = Bot(token=TELEGRAM_BOT_TOKEN)


def run_rita_main_with_logging():
    process = subprocess.Popen(
        ["python3", str(MAIN_SCRIPT_PATH)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        encoding="utf-8",
    )

    def log_output():
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            for line in process.stdout:
                log_file.write(line)
                log_file.flush()
                lowered = line.lower()
                if any(keyword in lowered for keyword in ["telegram", "conflict", "error"]):
                    logger.info(f"[TELEGRAM LOG] {line.strip()}")

    threading.Thread(target=log_output, daemon=True).start()
    return process


# Запуск процесса
process = run_rita_main_with_logging()



import signal
import subprocess
import psutil
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


import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def check_and_fix_main_script():
    path = os.path.join(os.getcwd(), "rita_main.py")
    if not os.path.exists(path):
        logger.error("[ERROR] rita_main.py не найден для анализа")
        return

    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    # Проверка отсутствия asyncio.run(main())
    if "asyncio.run(main())" not in code:
        logger.info("[FIX] Добавляем asyncio.run(main()) в конец rita_main.py")
        if "async def main(" in code:
            code += (
                "\n\nif __name__ == '__main__':\n"
                "    import asyncio\n"
                "    asyncio.run(main())\n"
            )
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)
            logger.info("✅ Исправление вставлено.")
        else:
            logger.warning("[WARN] main() не найден в rita_main.py — пропускаем исправление.")
    else:
        logger.info("✅ asyncio.run(main()) уже присутствует — ничего не меняем.")

# Вызов функции
check_and_fix_main_script()

# Пути и настройки
import requests
import time
from pathlib import Path

LOG_FILE = Path("logs/rita_bot.log")
MAIN_SCRIPT_PATH = Path("./rita_main.py")
HELPER_SCRIPT_PATH = Path("./check_bot_diagnostics.py")
REPO_RAW_URL = "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main/"

# --- Логирование ---
logging.basicConfig(
    filename=str(LOG_FILE),
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)




# --- Логирование ---


import time
import logging
from pathlib import Path

# Путь к лог-файлу
LOG_FILE = Path("logs/rita_bot.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)  # Создаёт папку logs/, если её нет

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Формат логирования
log_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# Консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

# Файл
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# --- Функции логирования ---
def log_debug(msg):
    logger.debug(f"[DEBUG] {time.ctime()} - {msg}")

def log_info(msg):
    logger.info(f"[INFO] {time.ctime()} - {msg}")

def log_error(msg):
    logger.error(f"[ERROR] {time.ctime()} - {msg}")
    # Дублируем в лог-файл (если хочешь, но logger уже это делает)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[ERROR] {time.ctime()} - {msg}\n")
    except Exception:
        pass



# --- Автообновление скрипта ---




def auto_update_script(script_path: Path, repo_raw_url: str) -> bool:
    try:
        log_info(f"Попытка автообновления: {getattr(script_path, 'name', None)}")
        raw_url = f"{repo_raw_url}/{getattr(script_path, 'name', None)}"
        response = requests.get(raw_url, timeout=15)
        if response.status_code != 200:
            log_error(f"Не удалось скачать raw файл {getattr(script_path, 'name', None)}, статус {response.status_code}")
            return False
        new_code = response.text
        if script_path.exists():
            current_code = script_path.read_text(encoding="utf-8")
            if new_code == current_code:
                log_info(f"{getattr(script_path, 'name', None)} уже актуален")
                return False
        script_path.write_text(new_code, encoding="utf-8")
        log_info(f"{getattr(script_path, 'name', None)} успешно обновлён")
        return True
    except Exception as e:
        log_error(f"Ошибка автообновления {getattr(script_path, 'name', None)}: {e}")
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
        r = requests.get(
            "https://api-inference.huggingface.co/models",
            headers={"Authorization": f"Bearer {HF_API_KEY}"}
        )
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
    url = f"https://safe_path_join(www.googleapis.com, customsearch)/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q=test"
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
    repo_raw_url = "https://safe_path_join(github.com, DeViLs9966)/rita_mega_bot"
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
    repo_raw_url = "https://safe_path_join(github.com, DeViLs9966)/rita_mega_bot"
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
        r = requests.get("https://api-inference.huggingface.co/models", headers=headers)
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
    url = f"https://safe_path_join(www.googleapis.com, customsearch)/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q=test"
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
        script_name = getattr(script_path, 'name', str(script_path))
        log_info(f"Попытка автообновления: {script_name}")

        if shutil.which("git") is not None:
            script_dir = safe_get_parent(script_path)
            if safe_path_join(script_dir, ".git").exists():
                log_debug(f"Выполняем git pull в {script_dir}")
                subprocess.run(["git", "-C", str(script_dir), "pull"], check=True)
                log_info(f"{script_name} обновлён через git pull")
                return True

        raw_url = repo_url.rstrip("/") + "/" + script_name
        log_debug(f"Скачиваем raw файл по URL: {raw_url}")
        r = requests.get(raw_url, timeout=15)
        if r.status_code == 200:
            script_path.write_text(r.text, encoding="utf-8")
            log_info(f"{script_name} обновлён через загрузку raw")
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
        log_debug("Выполнена safe_path_join(команда, proverka)")
    except Exception as e:
        await update.message.reply_text(f"❌ safe_path_join(Ошибка, pro): {e}")
        log_error(f"Ошибка safe_path_join(в, pro): {e}")
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
log_debug("Выполнена safe_path_join(команда, proverka)")
async def cmd_update_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return
    await update.message.reply_text("📥 Обновление rita_main.py...")
    updated = auto_update_script(
        MAIN_SCRIPT_PATH,
        "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main/rita_main.py"
    )
    if updated:
        await update.message.reply_text("✅ rita_main.py обновлён.")
    else:
        await update.message.reply_text("ℹ️ rita_main.py без изменений.")
async def cmd_update_self(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != OWNER_TELEGRAM_ID:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return
    await update.message.reply_text("📥 Обновление check_bot_diagnostics.py...")
    updated = auto_update_script(
        DIAGNOSTICS_SCRIPT_PATH,
        "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main/check_bot_diagnostics.py"
    )
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
        log_error(f"Ошибка хэша {getattr(path, "name", None)}: {e}")
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
import asyncio
import subprocess
import sys
async def auto_fix_and_restart_if_needed():
    global last_main_hash, last_diag_hash
    while True:
        await asyncio.sleep(300)  # Ждем 5 минут
        current_main_hash = calculate_hash(MAIN_SCRIPT_PATH)
        current_diag_hash = calculate_hash(DIAGNOSTICS_SCRIPT_PATH)
        # Проверяем изменения в основном скрипте
        if current_main_hash != last_main_hash:
            last_main_hash = current_main_hash
            log_info("Обнаружено изменение в rita_main.py, пытаемся обновить")
            updated = auto_update_script(
                MAIN_SCRIPT_PATH,
                "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main/rita_main.py"
            )
            if updated:
                log_info("rita_main.py обновлен, перезапуск...")
                try:
                    subprocess.Popen([sys.executable, str(MAIN_SCRIPT_PATH)])
                    log_info("rita_main.py перезапущен успешно")
                except Exception as e:
                    log_error(f"Ошибка при перезапуске rita_main.py: {e}")
        # Проверяем изменения во вспомогательном скрипте
        if current_diag_hash != last_diag_hash:
            last_diag_hash = current_diag_hash
            log_info("Обнаружено изменение в check_bot_diagnostics.py, пытаемся обновить")
            updated = auto_update_script(
                DIAGNOSTICS_SCRIPT_PATH,
                "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main/check_bot_diagnostics.py"
            )
            if updated:
                log_info("check_bot_diagnostics.py обновлен")
# --- Логирование ---


import requests
import json
import time
import logging
from pathlib import Path

# Лог-файл
LOG_FILE = Path("logs/rita_bot.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)  # Создаём папку logs при необходимости

# Настройка логгера
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),  # Вывод в консоль
        logging.FileHandler(LOG_FILE, encoding="utf-8")  # Лог в файл
    ]
)

# Функции логирования
def log_debug(msg):
    logging.debug(f"[DEBUG] {time.ctime()} - {msg}")

def log_info(msg):
    logging.info(f"[INFO] {time.ctime()} - {msg}")

def log_error(msg):
    logging.error(f"[ERROR] {time.ctime()} - {msg}")




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
        r = requests.get(
            "https://api-inference.huggingface.co/models",
            headers=headers
        )
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
        r = requests.get("https://safe_path_join(www.googleapis.com, customsearch)/v1", params=params, timeout=10)
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
        filename = getattr(script_path, "name", None)
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
        log_error(f"Ошибка автообновления {getattr(script_path, 'name', None)}: {e}")
        return False


# check_bot_diagnostics.py — блок 4 из 6 (полный и расширенный)
import threading
import hashlib
import time
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
# Обработка safe_path_join(команды, pro) — расширенная проверка систем и уведомление админа
async def handle_command_pro(update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="У вас нет доступа к этой команде."
        )
        log_info(f"Автообновления: попытка доступа запрещена для пользователя {user_id}")
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Запущена расширенная диагностика системы..."
    )
    log_info("Запущена команда /pro")
    # Проверки состояния систем
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
# Обработка safe_path_join(команды, proverka) — проверка и исправление (самообновление)
# Функция обработки safe_path_join(команды, proverka) — проверка и обновление скриптов
async def handle_command_proverka(update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_TELEGRAM_ID:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⛔ У вас нет доступа к этой команде."
        )
        log_info(f"[WARN] Попытка доступа к /proverka от {user_id}")
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🔍 Запущена проверка и обновление скриптов..."
    )
    repo_raw_url = "https://raw.githubusercontent.com/DeViLs9966/rita_mega_bot/main"
    updated_main = auto_update_script(MAIN_SCRIPT_PATH, repo_raw_url)
    updated_helper = auto_update_script(HELPER_SCRIPT_PATH, repo_raw_url)
    msg = "📦 Обновление завершено:\n"
    msg += f"├ Основной скрипт: {'✅ обновлён' if updated_main else 'ℹ️ без изменений'}\n"
    msg += f"└ Вспомогательный скрипт: {'✅ обновлён' if updated_helper else 'ℹ️ без изменений'}"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg
    )
    log_info("✅ Команда /proverka выполнена, результат отправлен.")
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
# Лог-функции (пример, можно использовать свои)
def log_info(msg):
    logger.info(f"[INFO] {msg}")
def log_error(msg):
    logger.info(f"[ERROR] {msg}")
# Ключ OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Пути к скриптам и логу
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
LOG_FILE_PATH = Path("safe_path_join(logs, rita_bot).log")
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
        error_report = analyze_errors_for_self_learning()  # должна быть синхронной функцией
        await send_admin_message(error_report)  # асинхронная
        repo_raw_url = "https://safe_path_join(raw.githubusercontent.com, DeViLs9966)/safe_path_join(rita_mega_bot, main)/"
        updated_main = auto_update_script(MAIN_SCRIPT_PATH, repo_raw_url)
        updated_helper = auto_update_script(HELPER_SCRIPT_PATH, repo_raw_url)
        fixed_main = await analyze_and_fix_script(MAIN_SCRIPT_PATH)
        fixed_helper = await analyze_and_fix_script(HELPER_SCRIPT_PATH)
        if updated_main or fixed_main:
            await restart_main_script()  # асинхронная функция для перезапуска основного скрипта
        if updated_helper or fixed_helper:
            await send_admin_message("🛠 check_bot_diagnostics.py был обновлён и перезапущен.")
        log_info("✅ Цикл самоулучшения завершён.")
    except Exception as e:
        log_error(f"❌ Ошибка в цикле самоулучшения: {e}")
# check_bot_diagnostics.py — БЛОК 5 из 6


import time
import subprocess
import sys
import json
import requests
import socket
from pathlib import Path

LOG_FILE = Path("logs/rita_bot.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def log_error(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"[ERROR] {time.ctime()}: {message}\n")
    print(f"[ERROR] {message}")

def log_info(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"[INFO] {time.ctime()}: {message}\n")
    print(f"[INFO] {message}")



# --- Самообучение: анализ логов ---





def analyze_errors_for_self_learning() -> str:
    try:
        if not LOG_FILE.exists():
            return "❌ Лог-файл не найден для анализа."

        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        error_lines = [line for line in lines if "[ERROR]" in line]

        # Очищаем сообщения от даты и времени
        cleaned_errors = []
        for line in error_lines:
            parts = line.split("] ")
            if len(parts) > 1:
                cleaned_errors.append(parts[-1].strip())
            else:
                cleaned_errors.append(line.strip())

        # Считаем частоту
        error_summary = {}
        for err in cleaned_errors:
            error_summary[err] = error_summary.get(err, 0) + 1

        # Сортируем
        sorted_errors = sorted(error_summary.items(), key=lambda x: x[1], reverse=True)

        # Формируем отчёт
        report = "📋 Отчёт самообучения: частота повторяющихся ошибок:\n\n"
        for err, count in sorted_errors[:50]:  # можешь менять лимит
            report += f"{count}×: {err}\n"

        return report.strip()

    except Exception as e:
        log_error(f"Ошибка анализа логов: {e}")
        return "❌ Ошибка при анализе логов."











# --- Обновление скрипта с GitHub ---






import subprocess
import requests
import shutil
from pathlib import Path

def auto_update_script(script_path: Path, repo_raw_url: str) -> bool:
    try:
        filename = script_path.name
        log_info(f"Попытка автообновления: {filename}")

        # Проверка наличия git и git-репозитория
        if shutil.which("git") is not None:
            script_dir = script_path.parent
            git_folder = script_dir / ".git"
            if git_folder.exists():
                log_info(f"Выполняем git pull в {script_dir}")
                subprocess.run(["git", "-C", str(script_dir), "pull"], check=True)
                log_info(f"{filename} обновлён через git pull")
                return True

        # Если git нет или репо не существует — скачиваем raw
        raw_url = repo_raw_url.rstrip("/") + "/" + filename
        log_info(f"Скачиваем raw файл по URL: {raw_url}")
        response = requests.get(raw_url, timeout=15)

        if response.status_code == 200:
            new_code = response.text
            current_code = ""
            if script_path.exists():
                current_code = script_path.read_text(encoding="utf-8")
            if new_code != current_code:
                script_path.write_text(new_code, encoding="utf-8")
                log_info(f"{filename} обновлён через загрузку raw")
                return True
            else:
                log_info(f"{filename} уже актуален")
                return False
        else:
            log_error(f"Не удалось скачать raw файл: статус {response.status_code}")
            return False
    except Exception as e:
        log_error(f"Ошибка автообновления {filename}: {e}")
        return False






# --- Перезапуск основного скрипта ---



import sys
import asyncio
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

MAIN_SCRIPT_PATH = Path("rita_main.py")

async def restart_main_script():
    try:
        logger.info("🔁 Перезапуск основного скрипта rita_main.py")
        process = await asyncio.create_subprocess_exec(
            sys.executable, str(MAIN_SCRIPT_PATH)
        )
        await send_admin_message("rita_main.py был автоматически перезапущен.")
    except Exception as e:
        logger.error(f"Ошибка перезапуска основного скрипта: {e}")

def log_error(msg: str):
    logger.error(msg)

def get_script_version(script_path: Path) -> str:
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            first_line = f.readline()
        if first_line.startswith("# Version:"):
            return first_line.strip().split(":", 1)[1].strip()
        return "unknown"
    except Exception as e:
        log_error(f"Ошибка получения версии {script_path.name}: {e}")
        return "error"









import asyncio
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

async def background_error_log_analysis():
    while True:
        try:
            log_file = Path("logs/rita_bot.log")  # исправлен путь к логу
            if log_file.exists():
                with open(log_file, "r", encoding="utf-8") as f:
                    log_text = f.read()
                errors = parse_error_logs(log_text)  # твоя функция разбора ошибок
                if errors:
                    fixes = generate_fixes_for_errors(errors)  # твоя функция генерации фиксов
                    if fixes:
                        apply_fixes(fixes)  # твоя функция применения фиксов
                        await send_admin_message("🛠 Автоматические исправления применены.")
            else:
                logger.warning(f"Файл лога не найден: {log_file}")
            await asyncio.sleep(300)  # пауза 5 минут между проверками
        except Exception as e:
            logger.error(f"[ERROR] Ошибка в background_error_log_analysis: {e}")
            await asyncio.sleep(60)  # при ошибке ждем минуту и пытаемся снова










# --- Полный цикл самообучения и автообновления ---
async def run_self_improvement_cycle():
    try:
        error_report = analyze_errors_for_self_learning()
        await send_admin_message(error_report)
        repo_raw_url = Path("https://safe_path_join(github.com, DeViLs9966)/rita_mega_bot")
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
import requests
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
    url = f"https://safe_path_join(www.googleapis.com, customsearch)/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q=test"
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
# --- Фоновое safe_path_join(автообновление, обучение) ---
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

    app = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .concurrent_updates(True)
        .close_loop(False)
        .build()
    )

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

    # Запуск бота
    await app.run_polling()



# --- Обработка Ctrl+safe_path_join(C, SIGTERM) ---
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
import time
LOG_FILE_PATH = "safe_path_join(logs, rita_bot).log"  # путь к файлу логов, где скрипт пишет ошибки
DIAGNOSTIC_SCRIPT_PATH = Path("check_bot_diagnostics.py")


import re
from pathlib import Path

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
        re.compile(r"Conflict: terminated by other getUpdates request"),  # специфичная ошибка Telegram
        # Можно добавить другие паттерны ошибок
    ]

    try:
        with open(log_path, "r", encoding="utf-8") as log_file:
            lines = log_file.readlines()
        buffer = []
        capture_traceback = False

        for line in lines:
            line = line.strip()
            # Если строка содержит паттерн ошибки — начинаем накапливать
            if any(p.search(line) for p in error_patterns):
                buffer.append(line)
                if "Traceback" in line:
                    capture_traceback = True
                continue

            if capture_traceback:
                # Если мы в режиме захвата трассировки, собираем строки
                buffer.append(line)
                if line == "":
                    # Пустая строка — конец трассировки, добавляем накопленное
                    errors.append("\n".join(buffer))
                    buffer.clear()
                    capture_traceback = False
            else:
                # Если есть накопленные строки, а текущая не ошибка — закрываем буфер
                if buffer:
                    errors.append("\n".join(buffer))
                    buffer.clear()

        # Если что-то осталось в буфере — добавляем
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





from pathlib import Path

def apply_fixes(fixes):
    """
    Вносит исправления в соответствующие скрипты.
    fixes — словарь вида { "путь_к_скрипту": [список_исправлений_строк] }
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
                    f.write(fix + "\n")
            results.append(f"[INFO] Внесены исправления в {script}.")
        except Exception as e:
            results.append(f"[ERROR] Ошибка при записи в {script}: {e}")
    return results








import shutil
import difflib
import ast
from pathlib import Path
import logging
from utils.fix_syntax import fix_unclosed_syntax  # импорт вашей функции автофикса синтаксиса

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

async def analyze_and_fix_script(script_path: Path, log_path: Path) -> bool:
    """
    Анализирует ошибки из лога и пытается исправить синтаксические ошибки в скрипте.
    Возвращает True, если были внесены изменения и сохранён исправленный файл, иначе False.
    """
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

        # Автофикс отсутствующего ":" в async def
        if "SyntaxError: expected ':'" in log_content:
            lines = fixed_code.splitlines()
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith("async def") and not stripped.endswith(":"):
                    lines[i] = line + ":"
                    logger.info(f"[FIX] Добавлен ':' в строке {i + 1}")
            fixed_code = "\n".join(lines)

        # Автофикс незакрытых f-строк (пример)
        if "unterminated string literal" in log_content:
            lines = fixed_code.splitlines()
            for i, line in enumerate(lines):
                if 'f"' in line and not line.strip().endswith('"'):
                    lines[i] = line + '"'
                    logger.info(f"[FIX] Закрыта f-строка в строке {i + 1}")
            fixed_code = "\n".join(lines)

        # Проверка компиляции текущего кода
        try:
            compile(fixed_code, str(script_path), 'exec')
        except SyntaxError as e:
            msg = str(e)
            # Попытка автофикса незакрытых скобок/кавычек
            if "was never closed" in msg or "unexpected EOF" in msg:
                logger.warning(f"[WARN] Обрыв конструкции: {msg}")
                fixed_code2 = fix_unclosed_syntax(fixed_code)
                try:
                    compile(fixed_code2, str(script_path), 'exec')
                    # Создание резервной копии
                    backup_path = script_path.with_suffix(script_path.suffix + ".backup")
                    shutil.copy(script_path, backup_path)
                    logger.info(f"[BACKUP] Создана резервная копия: {backup_path}")
                    # Сохранение исправленного кода
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

        # Проверяем синтаксис с помощью ast
        try:
            ast.parse(fixed_code)
        except SyntaxError as e:
            logger.error(f"[FAIL] Синтаксическая ошибка после всех попыток: {e}")
            return False

        # Если код изменён, сохраняем и выводим diff
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









from pathlib import Path

async def try_fix_syntax_errors(script_path: Path, logger) -> bool:
    code = script_path.read_text(encoding='utf-8')

    # Вынес fix_unclosed_syntax из вложенности, чтобы она была доступна
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
                logger.info(f"[FIX] Исправлены незакрытые скобки и кавычки в {script_path}")
                await send_admin_message(f"🛠️ Автофикс: исправлены незакрытые конструкции в {script_path.name}")
                return True
            except SyntaxError as e2:
                logger.error(f"[FAIL] Ошибка после попытки исправления: {e2}")
                return False
        else:
            logger.error(f"[FAIL] Синтаксическая ошибка: {msg}")
            return False
    except Exception as e:
        logger.error(f"[ERROR] analyze_and_fix_script: {e}")
        return False

def try_fix_syntax_errors_sync(script_path: str, logger=None):
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








async def ai_auto_improve():
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
                "Если есть проблемы, устаревшие участки, неэффективности или уязвимости, "
                "вноси правки прямо в код. Сохрани все функции. Автоматизируй и улучшай, "
                "но не удаляй ничего важного."
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
import asyncio
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, filters
# Предполагается, что nest_asyncio уже применён в основном скрипте
# Константы (укажи свои, если уже есть, тогда просто пропусти)
AUTHORIZED_USERS = [ ]  # Твой Telegram ID
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
def _is_authorized(update: Update) -> bool:
    try:
        return update.effective_user.id in AUTHORIZED_USERS
    except Exception as e:
        logger.warning(f"Authorization check failed: {e}")
        return False
async def auto_backup_and_push():
    try:
        logger.info("🔄 Выполняю git safe_path_join(add, commit)/push...")
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











import os
import re
from datetime import datetime
from pathlib import Path

IMPROVEMENT_LOG = Path("logs/rita_bot.log")  # исправил на реальный путь
ERROR_LOG_PATH = Path("logs/rita_bot.log")  # то же

async def self_improve_from_logs():
    logger.info("🤖 Начинаю анализ логов для саморазвития...")
    if not ERROR_LOG_PATH.exists():
        logger.info("ℹ️ Лог-файл не найден, пропускаю анализ.")
        return
    try:
        with open(ERROR_LOG_PATH, "r", encoding="utf-8") as f:
            logs = f.read()
        suggestions = []

        # Пример: найти повторяющиеся ошибки с паттерном
        pattern = re.findall(r"❌ Ошибка запуска бота: (.+)", logs)
        frequent_errors = {err: pattern.count(err) for err in set(pattern)}

        for error, count in frequent_errors.items():
            if count > 3:
                suggestions.append(f"Частая ошибка: {error} — встречается {count} раз.")

        # Проверка необработанных команд
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

# Константы для Telegram
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID
OWNER_ID = 558079551  # твой Telegram ID









from pathlib import Path
from telegram.constants import ParseMode
import logging

logger = logging.getLogger(__name__)
OWNER_ID = 558079551  # твой Telegram ID

async def send_admin_detailed_report(context):
    try:
        log_path = Path("logs/rita_bot.log")  # актуальный путь к логам
        if not log_path.exists():
            await context.bot.send_message(
                chat_id=OWNER_ID,
                text="✅ Лог файл не найден. Всё работает стабильно.",
                parse_mode=ParseMode.HTML
            )
            return

        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        errors = {}
        improvements = {}

        for idx, line in enumerate(lines, start=1):
            lower = line.lower()
            if "[error]" in lower:
                key = line.strip()
                if key not in errors:
                    errors[key] = {"count": 0, "lines": []}
                errors[key]["count"] += 1
                errors[key]["lines"].append(idx)
            elif "[fix]" in lower or "[info]" in lower or "улучш" in lower:
                key = line.strip()
                if key not in improvements:
                    improvements[key] = {"count": 0, "lines": []}
                improvements[key]["count"] += 1
                improvements[key]["lines"].append(idx)

        def format_section(title, data_dict):
            if not data_dict:
                return f"<b>{title}:</b>\nНет записей.\n\n"
            result = f"<b>{title} (всего {sum(v['count'] for v in data_dict.values())}):</b>\n"
            for text, info in sorted(data_dict.items(), key=lambda x: x[1]['count'], reverse=True):
                lines_sample = ", ".join(str(n) for n in info["lines"][:5])  # первые 5 номеров строк
                short_text = text if len(text) < 100 else text[:97] + "..."
                result += f" - <b>{info['count']}</b> раз (строки {lines_sample}): {short_text}\n"
            return result + "\n"

        report = ""
        report += format_section("Ошибки", errors)
        report += format_section("Улучшения и информационные записи", improvements)

        if not errors and not improvements:
            report = "✅ Лог пуст или не содержит ошибок и улучшений."

        # Ограничиваем длину сообщения (макс 4096 символов для Telegram)
        if len(report) > 4000:
            report = report[:3997] + "..."

        await context.bot.send_message(
            chat_id=OWNER_ID,
            text=report,
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        logger.error(f"⚠️ Ошибка при отправке подробного отчёта админу: {e}")












import aiohttp
import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = "твой_токен"
TELEGRAM_CHAT_ID = 558079551
LOG_FILE_PATH = "path/to/rita_bot.log"
MAIN_SCRIPT_PATH = "rita_main.py"
IMPROVEMENTS_DIR = "improvements"

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
    errors - список строк с ERROR или Exception
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
        needed_functions = [
            "async def run_bot(",
            "async def auto_fix_loop(",
            "async def auto_fix_and_restart_if_needed(",
            "asyncio.create_task(",
        ]
        for func in needed_functions:
            if func not in content:
                problems.append(f"Отсутствует ключевая функция или вызов: {func}")
    except Exception as e:
        problems.append(f"Ошибка при чтении основного скрипта: {e}")
    if problems:
        logger.warning("Проблемы в основном скрипте: " + "; ".join(problems))
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
        os.makedirs(IMPROVEMENTS_DIR, exist_ok=True)
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
    Делает git safe_path_join(add, commit)/push основного скрипта и улучшений.
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
import re
from datetime import datetime
async def analyze_and_improve_full():
    """
    Полный анализ, генерация улучшений, отправка отчётов, бэкап и пуш.
    Включает номера строк, контекст ошибок и диапазон строк улучшений.
    """
    log_lines = read_log_tail(500)
    errors, successes = detect_errors_and_successes(log_lines)
    script_problems = check_main_script_health()
    report = "<b>📊 Отчет об анализе Rita Mega Bot</b>\n"
    report += f"<i>Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</i>\n\n"
    # ✅ Успехи
    report += "<b>✅ Успешные действия (последние 10):</b>\n"
    if successes:
        report += "\n".join(successes[-10:]) + "\n\n"
    else:
        report += "Нет зафиксированных успешных событий.\n\n"
    # ❌ Ошибки с анализом строк
    report += "<b>❌ Ошибки (последние 10):</b>\n"
    if errors:
        error_analysis = []
        for err in errors[-10:]:
            match = re.search(r'File "(.+)", line (\d+)', err)
            if match:
                file_name = match.group(1)
                line_num = int(match.group(2))
                error_analysis.append(f"{file_name}, строка {line_num}: {err.strip()}")
            else:
                error_analysis.append(err.strip())
        report += "\n".join(error_analysis) + "\n\n"
    else:
        report += "Ошибок не обнаружено.\n\n"
    # 🔍 Анализ проблем скрипта
    report += "<b>🧠 Проблемы с кодом скрипта:</b>\n"
    if script_problems:
        report += "\n".join(script_problems) + "\n\n"
    else:
        report += "Проблем с основным кодом не найдено.\n\n"
    # 🛠 Генерация улучшений
    improvements_created = []
    if script_problems or errors:
        report += "<b>🛠 Сгенерированные улучшения:</b>\n"
        # Пример улучшения: добавить автообновление если его нет
        auto_update_code = generate_auto_update_improvement()
        fname = create_improvement_file(auto_update_code, "auto_update")
        if fname:
            improvements_created.append(fname)
            report += f"Создано улучшение: <code>{fname}</code> (автообновление).\n"
        else:
            report += "Не удалось сгенерировать код улучшения.\n"
    else:
        report += "Улучшения не требуются — всё работает стабильно.\n"
    # 📤 Отправка отчета
    await send_telegram_message(report)
    logger.info("📤 Подробный отчет отправлен в Telegram.")
    # 💾 Git backup и push
    success, msg = do_git_backup_and_push()
    if success:
        await send_telegram_message(f"✅ Git backup и push прошли успешно.")
    else:
        await send_telegram_message(f"⚠️ Git safe_path_join(backup, push) не выполнен:\n{msg}")
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
import re
import subprocess
import aiohttp
import asyncio
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
LOG_FILE = "safe_path_join(logs, rita_bot).log"  # путь к логу твоего основного бота (проверь точный)
MAIN_SCRIPT = "/safe_path_join(mnt, data)/safe_path_join(rita_mega_bot, rita_main).py"    # путь к основному скрипту
GIT_REPO_PATH = "/safe_path_join(mnt, data)/rita_mega_bot"               # путь к git-репозиторию с твоим ботом
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"  # твой реальный токен
TELEGRAM_ADMIN_ID = 558079551  # твой Telegram ID, число без кавычек
bot = Bot(token="7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")
# Функция для отправки сообщения в телеграм














import os
import re
import asyncio
import subprocess
from pathlib import Path
from telegram.constants import ParseMode

# Константы — подкорректируй под свой проект
LOG_FILE = Path("logs/rita_bot.log")  # или safe_path_join(logs, rita_bot).log
MAIN_SCRIPT = Path("rita_main.py")
OWNER_ID = 558079551
GIT_REPO_PATH = Path(".")  # Путь к корню репозитория

# Логгер (если нет, создай)
import logging
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logging.basicConfig(level=logging.INFO)

# Отправка сообщения в Telegram
async def send_telegram_message(bot, text: str):
    try:
        await bot.send_message(chat_id=OWNER_ID, text=text, parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(f"[Telegram send error]: {e}")

# Анализ лога для ошибок и предупреждений
async def analyze_logs():
    if not LOG_FILE.exists():
        return "⚠️ Лог файл не найден!"
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.read()
        errors = re.findall(r"(?i)(error|exception|fail|critical)", logs)
        warnings = re.findall(r"(?i)(warning|warn|deprecated)", logs)
        result = f"🔍 Анализ логов:\nОшибок найдено: {len(errors)}\nПредупреждений: {len(warnings)}"
        return result
    except Exception as e:
        logger.error(f"Ошибка анализа логов: {e}")
        return "⚠️ Ошибка при анализе логов."

# Проверка наличия ключевых функций в основном скрипте
async def check_main_script_functions():
    required_functions = [
        "async def run_bot",
        "async def auto_fix_loop",
        "async def auto_fix_and_restart_if_needed",
        "async def start_monitoring_thread",
        # добавляй сюда свои важные функции
    ]

    if not MAIN_SCRIPT.exists():
        return "⚠️ Основной скрипт не найден!"

    try:
        with open(MAIN_SCRIPT, "r", encoding="utf-8") as f:
            main_code = f.read()
    except Exception as e:
        logger.error(f"Ошибка чтения основного скрипта: {e}")
        return "⚠️ Ошибка чтения основного скрипта."

    missing = [func for func in required_functions if func not in main_code]

    if not missing:
        return "✅️️ Все ключевые функции присутствуют в основном скрипте."
    else:
        miss_list = "\n".join(missing)
        return f"⚠️ Отсутствуют функции:\n{miss_list}"

# Добавление функции в основной скрипт (если её нет)
async def add_missing_function(func_code: str, func_name: str):
    if not MAIN_SCRIPT.exists():
        logger.error(f"Основной скрипт {MAIN_SCRIPT} не найден для добавления функции.")
        return False
    try:
        with open(MAIN_SCRIPT, "r", encoding="utf-8") as f:
            main_code = f.read()
        if func_name in main_code:
            return False  # функция уже есть
        with open(MAIN_SCRIPT, "a", encoding="utf-8") as f:
            f.write("\n\n" + func_code.strip() + "\n")
        logger.info(f"Функция '{func_name}' добавлена в основной скрипт.")
        return True
    except Exception as e:
        logger.error(f"Ошибка при добавлении функции '{func_name}': {e}")
        return False

# Чтение всего лога (для других целей)
def read_full_log():
    if not LOG_FILE.exists():
        logger.warning(f"Лог-файл {LOG_FILE} не найден")
        return []
    try:
        with open(LOG_FILE, encoding="utf-8") as f:
            return f.readlines()
    except Exception as e:
        logger.error(f"Ошибка чтения лога: {e}")
        return []

# Анализ логов с указанием строк ошибок и успешных действий (можно продолжить реализацию)

# Пример: добавь сюда функции для автофикса, коммитов, перезапуска и т.д.










import asyncio
import subprocess
import logging
import re
import os
import sys
from pathlib import Path
from telegram.constants import ParseMode

logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logging.basicConfig(level=logging.INFO)

OWNER_ID = 558079551
GIT_REPO_PATH = Path(".")
LOG_FILE = Path("logs/rita_bot.log")
MAIN_SCRIPT = Path("rita_main.py")
DIAGNOSTICS_SCRIPT = Path("check_bot_diagnostics.py")

REQUIRED_FUNCTIONS = {
    MAIN_SCRIPT: [
        "async def run_bot",
        "async def auto_fix_loop",
        "async def auto_fix_and_restart_if_needed",
        "async def start_monitoring_thread",
    ],
    DIAGNOSTICS_SCRIPT: [
        "async def auto_fix_loop",
        "async def self_improve_from_logs",
    ],
}

# --- Анализ логов с выявлением частых ошибок и предупреждений ---
def analyze_log_details(log_lines):
    errors = []
    successes = []
    error_counter = {}
    warning_counter = {}

    for i, line in enumerate(log_lines, start=1):
        low_line = line.lower()
        if "[error]" in low_line or "traceback" in low_line or "exception" in low_line:
            errors.append(f"Строка {i}: {line.strip()}")
            err_key = line.strip()
            error_counter[err_key] = error_counter.get(err_key, 0) + 1
        elif "[warn]" in low_line or "deprecated" in low_line:
            warn_key = line.strip()
            warning_counter[warn_key] = warning_counter.get(warn_key, 0) + 1
        elif "[info]" in low_line or "[success]" in low_line or "started" in low_line or "complete" in low_line:
            successes.append(f"Строка {i}: {line.strip()}")

    # Часто встречающиеся ошибки (>3 раза)
    frequent_errors = {k: v for k, v in error_counter.items() if v > 3}
    frequent_warnings = {k: v for k, v in warning_counter.items() if v > 3}

    return errors, successes, frequent_errors, frequent_warnings

# --- Проверка состояния основных скриптов и ключевых функций ---
def check_scripts_health():
    problems = []

    for script_path, funcs in REQUIRED_FUNCTIONS.items():
        if not script_path.exists():
            problems.append(f"❌ Скрипт {script_path} не найден.")
            continue
        try:
            with open(script_path, encoding="utf-8") as f:
                content = f.read()
            for func in funcs:
                if func not in content:
                    problems.append(f"⚠️ В {script_path.name} отсутствует ключевая функция: {func}")
        except Exception as e:
            problems.append(f"⚠️ Ошибка чтения {script_path.name}: {e}")

    return problems

# --- Отправка сообщения в Telegram ---



from telegram.ext import Application
import logging

logger = logging.getLogger(__name__)

async def send_telegram_message(text, app=None):
    try:
        if app is None:
            app = (
                Application.builder()
                .token(TELEGRAM_BOT_TOKEN)
                .concurrent_updates(True)
                .close_loop(False)
                .build()
            )
            await app.initialize()
            await app.start()

        # ✅ Разбиваем длинные сообщения на части по 3900 символов
        chunk_size = 3900
        for i in range(0, len(text), chunk_size):
            await app.bot.send_message(chat_id=OWNER_ID, text=text[i:i+chunk_size])

        logger.info("✅ Отчёт отправлен в Telegram.")

    except Exception as e:
        logger.error(f"❌ Ошибка при отправке сообщения в Telegram: {e}")




# --- Автофиксы: добавление недостающих функций в скрипты ---
async def apply_auto_fixes(app=None):
    fixes_applied = []
    # Примеры функций для автофикса, можно расширить
    auto_fix_functions = {
        DIAGNOSTICS_SCRIPT: '''
async def auto_fix_loop():
    while True:
        logger.info("Автофикс запущен.")
        await asyncio.sleep(3600)
''',
        MAIN_SCRIPT: '''
async def run_bot():
    # Пример заглушки запуска бота
    logger.info("Запуск бота...")
    # Твой основной код запуска бота здесь
''',
    }

    for script_path, func_code in auto_fix_functions.items():
        try:
            if not script_path.exists():
                # Создать файл, если отсутствует
                with open(script_path, "w", encoding="utf-8") as f:
                    f.write(func_code.strip() + "\n")
                fixes_applied.append(f"Создан файл {script_path.name} с функцией автофикса.")
                continue

            content = script_path.read_text(encoding="utf-8")
            func_name_line = func_code.strip().splitlines()[0]  # первая строка с async def
            if func_name_line not in content:
                with open(script_path, "a", encoding="utf-8") as f:
                    f.write("\n\n" + func_code.strip() + "\n")
                fixes_applied.append(f"Добавлена функция '{func_name_line}' в {script_path.name}")
        except Exception as e:
            fixes_applied.append(f"Ошибка при автофиксе {script_path.name}: {e}")

    if fixes_applied:
        await send_telegram_message("➕ Автофиксы применены:\n" + "\n".join(fixes_applied), app)
    else:
        await send_telegram_message("ℹ️ Автофиксы не требовались.", app)

    return len(fixes_applied) > 0

# --- Git commit и push с умной логикой ---
async def git_commit_and_push(commit_message="Автофикс и улучшения"):
    try:
        proc_add = subprocess.run(["git", "add", "."], capture_output=True, text=True)
        if proc_add.returncode != 0:
            logger.error(f"Git add failed:\n{proc_add.stderr}")
            return False, f"❌ Git add failed:\n{proc_add.stderr}"

        proc_commit = subprocess.run(
            ["git", "commit", "-m", commit_message],
            capture_output=True, text=True)
        if proc_commit.returncode != 0:
            if "nothing to commit" in proc_commit.stderr.lower():
                logger.info("Нет новых изменений для коммита.")
                return False, "ℹ️ Нет новых изменений для коммита."
            else:
                logger.error(f"Git commit failed:\n{proc_commit.stderr}")
                return False, f"❌ Git commit failed:\n{proc_commit.stderr}"

        proc_push = subprocess.run(["git", "push"], capture_output=True, text=True)
        if proc_push.returncode != 0:
            logger.error(f"Git push failed:\n{proc_push.stderr}")
            return False, f"❌ Git push failed:\n{proc_push.stderr}"

        logger.info("Изменения успешно запушены в GitHub.")
        return True, "✅ Изменения успешно запушены в GitHub."
    except Exception as e:
        logger.error(f"Ошибка git commit и push: {e}")
        return False, f"❌ Ошибка git commit и push: {e}"

# --- Перезапуск основного скрипта (если нужно) ---
async def restart_main_script():
    try:
        # Подкорректируй под свою систему и способ запуска
        # Пример для Unix систем с python3
        logger.info("Перезапуск основного скрипта...")
        python = sys.executable
        os.execv(python, [python, str(MAIN_SCRIPT)])
    except Exception as e:
        logger.error(f"Ошибка перезапуска скрипта: {e}")

# --- Полный цикл анализа, автофиксов, коммитов и перезапуска ---
async def full_analysis_and_improve(app=None):
    # Читаем лог
    if not LOG_FILE.exists():
        await send_telegram_message("⚠️ Лог-файл не найден, пропускаю анализ.", app)
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.readlines()

    errors, successes, frequent_errors, frequent_warnings = analyze_log_details(logs)
    health_problems = check_scripts_health()

    report = "<b>📝 Отчёт анализа:</b>\n"

    if errors:
        report += f"❌ Ошибки ({len(errors)}):\n" + "\n".join(errors[:10]) + ("\n..." if len(errors) > 10 else "") + "\n\n"
    else:
        report += "✅ Ошибок не обнаружено.\n\n"

    if successes:
        report += f"ℹ️ Успешные операции ({len(successes)}):\n" + "\n".join(successes[:10]) + ("\n..." if len(successes) > 10 else "") + "\n\n"

    if frequent_errors:
        report += "<b>Часто встречающиеся ошибки:</b>\n"
        for err, count in frequent_errors.items():
            report += f"- {count} раз: {err}\n"
        report += "\n"

    if frequent_warnings:
        report += "<b>Часто встречающиеся предупреждения:</b>\n"
        for warn, count in frequent_warnings.items():
            report += f"- {count} раз: {warn}\n"
        report += "\n"

    if health_problems:
        report += "⚠️ Проблемы со скриптами:\n" + "\n".join(health_problems) + "\n\n"
    else:
        report += "✅ Скрипты в порядке.\n\n"

    await send_telegram_message(report, app)

    fixes_needed = await apply_auto_fixes(app)
    if fixes_needed:
        success, msg = await git_commit_and_push()
        await send_telegram_message(msg, app)
        if success:
            # Перезапуск после фиксов
# Перезапуск после фиксов
            await send_telegram_message("♻️ Перезапуск основного скрипта после применения автофиксов...", app)
            await asyncio.sleep(2)  # Небольшая пауза перед перезапуском
            await restart_main_script()
    else:
        await send_telegram_message("✅ Автофиксы не потребовались. Перезапуск не нужен.", app)



















async def analyze_and_improve_full():
    try:
        log_lines = read_full_log()
        errors, successes = analyze_log_details(log_lines)
        script_problems = check_main_script_health()
        report = "<b>Отчёт об анализе Rita Mega Bot</b>\n\n"
        if successes:
            report += "<b>Успешные действия (последние 10):</b>\n" + "\n".join(successes[-10:]) + "\n\n"
        else:
            report += "Нет данных по успешным действиям.\n\n"
        if errors:
            report += "<b>Ошибки (последние 10):</b>\n" + "\n".join(errors[-10:]) + "\n\n"
        else:
            report += "Ошибок не обнаружено.\n\n"
        if script_problems:
            report += "<b>Проблемы с основным скриптом:</b>\n" + "\n".join(script_problems) + "\n\n"
        else:
            report += "Проблем не обнаружено.\n\n"
        await send_telegram_message(report)
        await auto_fix_and_commit()
        logger.info("✅ Цикл анализа и улучшения завершён.")
    except Exception as e:
        logger.error(f"❌ Ошибка в analyze_and_improve_full: {e}")
# --- Фоновая задача для периодического запуска ---
async def background_auto_fix_loop():
    while True:
        try:
            await analyze_and_improve_full()
        except Exception as e:
            logger.error(f"Ошибка в background_auto_fix_loop: {e}")
        await asyncio.sleep(300)  # каждые 5 минут
# В main async функцию твоего check_bot_diagnostics.py добавь запуск:
# asyncio.create_task(background_auto_fix_loop())
# Основная функция автоанализа и улучшения
async def run_intelligent_auto_improve():
    log_summary = await analyze_logs()
    script_check = await check_main_script_functions()
    await send_telegram_message("🔧 Автоанализ и проверка бота запущены...")
    await send_telegram_message(log_summary)
    await send_telegram_message(script_check)
    # Если функции отсутствуют - попробуем добавить и запушить



async def hourly_auto_improve_loop():
    logger.info("🔁 Цикл автоулучшения запущен.")
    while True:
        try:
            await improve_scripts_with_generated()
        except Exception as e:
            logger.error(f"[LOOP ERROR] {e}")
        await asyncio.sleep(3600)

async def main():
    asyncio.create_task(hourly_auto_improve_loop())
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        logger.info("🚪 Завершение по Ctrl+C")









































































    if "Отсутствуют функции" in script_check:
        await auto_fix_and_commit()
    else:
        await send_telegram_message("✅ Улучшений не требуется, скрипт в порядке.")
# Для запуска в asyncio

import asyncio
import nest_asyncio
import signal
import logging
import os

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
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Заглушки для автофикса — если у тебя есть настоящие, оставь их


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
import asyncio
import logging
import subprocess
import difflib
import shutil
import re
import os
import ast
import openai
from pathlib import Path
from datetime import datetime

# Логгер
logger = logging.getLogger("AutoImprove")
logging.basicConfig(level=logging.INFO)

# Настройки
OPENAI_API_KEY = "твой_ключ"
openai.api_key = OPENAI_API_KEY
OWNER_ID = 558079551
GIT_REPO_PATH = Path(".")
RITA_MAIN_PATH = Path("rita_main.py")
CHECK_DIAG_PATH = Path("check_bot_diagnostics.py")
LOG_PATH = Path("logs/bot.log")

def fix_unclosed_syntax(code: str) -> str:
    open_parens = code.count('(')
    close_parens = code.count(')')
    if open_parens > close_parens:
        code += ')' * (open_parens - close_parens)
    open_sq = code.count('[')
    close_sq = code.count(']')
    if open_sq > close_sq:
        code += ']' * (open_sq - close_sq)
    open_curly = code.count('{')
    close_curly = code.count('}')
    if open_curly > close_curly:
        code += '}' * (open_curly - close_curly)
    quote_count = code.count('"')
    if quote_count % 2 != 0:
        code += '"'
    return code

def remove_duplicate_or_conflicting_code(code1: str, code2: str) -> (str, str):
    lines1 = set(code1.splitlines())
    lines2 = set(code2.splitlines())
    unique1 = [line for line in code1.splitlines() if line not in lines2]
    unique2 = [line for line in code2.splitlines() if line not in lines1]
    return ("\n".join(unique1), "\n".join(unique2))

async def generate_new_functionality(existing_code_main: str, existing_code_diag: str) -> tuple[str, str]:
    prompt = f"""
Ты - эксперт в разработке Telegram-ботов и автообновляющихся систем.
У тебя есть два скрипта:
rita_main.py:
{existing_code_main[:1500]}...
check_bot_diagnostics.py:
{existing_code_diag[:1500]}...

На основе анализа текущего состояния, предложи улучшения. Создай по 1 новой функции для каждого файла:
- для rita_main.py: def new_func_main_...
- для check_bot_diagnostics.py: def new_func_diag_...

Каждую функцию выдай полностью, с комментариями.
"""
    try:
        logger.info("[AI] Запрос генерации новых функций...")
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.7,
        )
        content = response['choices'][0]['message']['content']
        main_func = re.search(r"(def new_func_main_[\s\S]*?)(?=\n\ndef new_func_diag_)", content)
        diag_func = re.search(r"(def new_func_diag_[\s\S]*)", content)
        return main_func.group(1).strip() if main_func else "", diag_func.group(1).strip() if diag_func else ""
    except Exception as e:
        logger.error(f"[AI] Ошибка генерации: {e}")
        return "", ""

def backup_file(path: Path):
    backup_path = path.with_suffix(path.suffix + ".bak")
    shutil.copy2(path, backup_path)

def append_if_missing(path: Path, func_code: str) -> bool:
    if not func_code.strip():
        return False
    content = path.read_text(encoding="utf-8")
    if func_code.strip().splitlines()[0] in content:
        logger.info(f"[SKIP] Функция уже существует в {path.name}")
        return False
    backup_file(path)
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n\n" + func_code.strip() + "\n")
    logger.info(f"[APPEND] Новая функция добавлена в {path.name}")
    return True

def git_commit_and_push(msg="Auto update"):
    subprocess.run(["git", "-C", str(GIT_REPO_PATH), "add", "."], capture_output=True)
    subprocess.run(["git", "-C", str(GIT_REPO_PATH), "commit", "-m", msg], capture_output=True)
    subprocess.run(["git", "-C", str(GIT_REPO_PATH), "push"], capture_output=True)

def restart_main_script():
    try:
        import psutil
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['cmdline'] and "rita_main.py" in " ".join(proc.info['cmdline']):
                logger.info(f"[KILL] Завершаем {proc.info['pid']} (rita_main.py)")
                proc.kill()
        logger.info("[RESTART] Перезапуск rita_main.py")
        subprocess.Popen(["python3", str(RITA_MAIN_PATH)])
    except Exception as e:
        logger.error(f"[RESTART FAIL] {e}")

async def improve_scripts_with_generated():
    logger.info("[RUN] Начинаем улучшение скриптов...")
    if not RITA_MAIN_PATH.exists() or not CHECK_DIAG_PATH.exists():
        logger.warning("❌ Один из файлов не найден")
        return
    main_code = RITA_MAIN_PATH.read_text(encoding="utf-8")
    diag_code = CHECK_DIAG_PATH.read_text(encoding="utf-8")
    main_func, diag_func = await generate_new_functionality(main_code, diag_code)

    changed = False
    if append_if_missing(RITA_MAIN_PATH, main_func):
        changed = True
    if append_if_missing(CHECK_DIAG_PATH, diag_func):
        changed = True

    if changed:
        git_commit_and_push("Auto: добавлены новые AI-функции")
        restart_main_script()
    else:
        logger.info("[OK] Новых функций не найдено или уже добавлены.")


async def hourly_auto_improve_loop():
    logger.info("🔁 Цикл автоулучшения запущен.")
    while True:
        try:
            await improve_scripts_with_generated()
        except Exception as e:
            logger.error(f"[LOOP ERROR] {e}")
        await asyncio.sleep(3600)

async def main():
    asyncio.create_task(hourly_auto_improve_loop())
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        logger.info("🚪 Завершение по Ctrl+C")


import asyncio
import logging
import difflib
import shutil
import ast
import re
from pathlib import Path
import openai

# --- Настройка ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OPENAI_API_KEY = "твой_ключ"
openai.api_key = OPENAI_API_KEY

RITA_MAIN_PATH = Path("rita_main.py")
CHECK_DIAG_PATH = Path("check_bot_diagnostics.py")
LOG_PATH = Path("logs/bot.log")

# --- Удаление дубликатов ---
def remove_duplicate_or_conflicting_code(code1: str, code2: str) -> tuple[str, str]:
    lines1 = set(code1.splitlines())
    lines2 = set(code2.splitlines())
    unique1 = [line for line in code1.splitlines() if line not in lines2]
    unique2 = [line for line in code2.splitlines() if line not in lines1]
    return "\n".join(unique1), "\n".join(unique2)

# --- Автофиксация незакрытых конструкций ---
def fix_unclosed_syntax(code: str) -> str:
    open_parens = code.count('(')
    close_parens = code.count(')')
    if open_parens > close_parens:
        code += ')' * (open_parens - close_parens)
    open_sq = code.count('[')
    close_sq = code.count(']')
    if open_sq > close_sq:
        code += ']' * (open_sq - close_sq)
    open_curly = code.count('{')
    close_curly = code.count('}')
    if open_curly > close_curly:
        code += '}' * (open_curly - close_curly)
    if code.count('"') % 2 != 0:
        code += '"'
    return code

# --- Генерация новых функций ---
async def generate_new_functionality(code_main: str, code_diag: str) -> tuple[str, str]:
    prompt = f"""
Ты эксперт Python Telegram-ботов. Есть два скрипта:
rita_main.py:
{code_main[:1500]}
---
check_bot_diagnostics.py:
{code_diag[:1500]}
---
Создай по одной полезной новой функции для каждого файла:
- Функция для rita_main.py: начинается с def new_func_main_
- Функция для check_bot_diagnostics.py: начинается с def new_func_diag_
Полный код с комментариями.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.7,
        )
        content = response["choices"][0]["message"]["content"]
        main_func = ""
        diag_func = ""
        main_match = re.search(r"(def new_func_main_[\s\S]+?)(?=\n\ndef new_func_diag_|$)", content)
        diag_match = re.search(r"(def new_func_diag_[\s\S]+)", content)

        if main_match:
            main_func = main_match.group(1).strip()
        if diag_match:
            diag_func = diag_match.group(1).strip()

        return main_func, diag_func
    except Exception as e:
        logger.error(f"[OpenAI ERROR]: {e}")
        return "", ""

# --- Анализ и исправление скрипта ---
async def analyze_and_fix_script(script_path: Path, log_path: Path) -> bool:
    try:
        if not script_path.exists():
            logger.warning(f"[WARN] Файл не найден: {script_path}")
            return False
        if not log_path.exists():
            logger.warning(f"[WARN] Лог-файл не найден: {log_path}")
            return False

        original_code = script_path.read_text(encoding="utf-8")
        fixed_code = original_code
        lines = fixed_code.splitlines()

        for i, line in enumerate(lines):
            if line.strip().startswith("async def") and not line.strip().endswith(":"):
                lines[i] += ":"
                logger.info(f"[FIX] Добавлен ':' в строке {i + 1}")
            if 'f"' in line and line.count('"') % 2 != 0:
                lines[i] += '"'
                logger.info(f"[FIX] Закрыта f-строка в строке {i + 1}")

        fixed_code = "\n".join(lines)

        try:
            compile(fixed_code, str(script_path), 'exec')
        except SyntaxError as e:
            msg = str(e)
            logger.warning(f"[SYNTAX WARNING] {msg}")
            fixed_code2 = fix_unclosed_syntax(fixed_code)
            try:
                compile(fixed_code2, str(script_path), 'exec')
                backup_path = script_path.with_suffix(".backup")
                shutil.copy(script_path, backup_path)
                script_path.write_text(fixed_code2, encoding="utf-8")
                logger.info(f"[FIX] Незакрытые конструкции исправлены и сохранены.")
                fixed_code = fixed_code2
            except SyntaxError as e2:
                logger.error(f"[FAIL] Ошибка после фикса: {e2}")
                return False

        try:
            ast.parse(fixed_code)
        except SyntaxError as e:
            logger.error(f"[FAIL] AST ошибка: {e}")
            return False

        if fixed_code != original_code:
            script_path.write_text(fixed_code, encoding="utf-8")
            diff = ''.join(difflib.unified_diff(
                original_code.splitlines(keepends=True),
                fixed_code.splitlines(keepends=True),
                fromfile=str(script_path),
                tofile=str(script_path) + " (исправлен)",
            ))
            logger.info(f"[DIFF] Изменения:\n{diff}")
            return True
        else:
            logger.info("[INFO] Изменений не требуется.")
            return False
    except Exception as e:
        logger.error(f"[ERROR] analyze_and_fix_script(): {e}")
        return False

# --- Основной запуск ---
async def main():
    logger.info("[START] Анализ и автофиксация начата")

    code_main = RITA_MAIN_PATH.read_text(encoding="utf-8") if RITA_MAIN_PATH.exists() else ""
    code_diag = CHECK_DIAG_PATH.read_text(encoding="utf-8") if CHECK_DIAG_PATH.exists() else ""

    code_main_unique, code_diag_unique = remove_duplicate_or_conflicting_code(code_main, code_diag)
    RITA_MAIN_PATH.write_text(code_main_unique, encoding="utf-8")
    CHECK_DIAG_PATH.write_text(code_diag_unique, encoding="utf-8")

    fixed_main = await analyze_and_fix_script(RITA_MAIN_PATH, LOG_PATH)
    fixed_diag = await analyze_and_fix_script(CHECK_DIAG_PATH, LOG_PATH)

    new_func_main, new_func_diag = await generate_new_functionality(code_main_unique, code_diag_unique)

    changed = False
    if new_func_main:
        with open(RITA_MAIN_PATH, "a", encoding="utf-8") as f:
            f.write("\n\n# --- Авто-сгенерированная функция ---\n")
            f.write(new_func_main + "\n")
        logger.info("[AI] Добавлена функция в rita_main.py")
        changed = True

    if new_func_diag:
        with open(CHECK_DIAG_PATH, "a", encoding="utf-8") as f:
            f.write("\n\n# --- Авто-сгенерированная функция ---\n")
            f.write(new_func_diag + "\n")
        logger.info("[AI] Добавлена функция в check_bot_diagnostics.py")
        changed = True

    if changed:
        shutil.copy(RITA_MAIN_PATH, RITA_MAIN_PATH.with_suffix(".backup"))
        shutil.copy(CHECK_DIAG_PATH, CHECK_DIAG_PATH.with_suffix(".backup"))
        logger.info("[BACKUP] Бэкапы созданы.")

    logger.info("[DONE] Завершено.")






































































import os
import asyncio
import signal
import logging
import nest_asyncio
from pathlib import Path
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram.error import Conflict

# --- Настройки и логгирование ---
os.makedirs('logs', exist_ok=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Константы ---
TELEGRAM_BOT_TOKEN = "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
TELEGRAM_ADMIN_ID = OWNER_ID = 558079551



















# --- Импорт необходимых функций ---







# auto_fix_tools.py


# Цвета для терминала (ANSI escape codes)
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_RED = "\033[31m"

def color_text(text: str, color_code: str) -> str:
    return f"{color_code}{text}{COLOR_RESET}"

class AutoFixReportEntry:
    def __init__(self, line: int, message: str, level: str = "INFO"):
        self.line = line
        self.message = message
        self.level = level.upper()

    def formatted(self):
        if self.level == "INFO":
            return color_text(f"[INFO] Line {self.line}: {self.message}", COLOR_GREEN)
        elif self.level == "WARNING":
            return color_text(f"[WARNING] Line {self.line}: {self.message}", COLOR_YELLOW)
        elif self.level == "ERROR":
            return color_text(f"[ERROR] Line {self.line}: {self.message}", COLOR_RED)
        else:
            return f"[{self.level}] Line {self.line}: {self.message}"

def parse_error_log(log_lines):
    error_entries = []

    for line in log_lines:
        line_num = None
        # Ищем номер строки ошибки в формате "line XX" или "at line XX"
        line_match = re.search(r'(?:line|at line) (\d+)', line, re.IGNORECASE)
        if line_match:
            line_num = int(line_match.group(1))
        else:
            line_num = -1

        line_lower = line.lower()

        # Определяем уровень и тип ошибки по ключевым словам
        if "syntaxerror" in line_lower:
            if "unterminated string literal" in line_lower:
                msg = "Незакрытая строка — пропущена кавычка или апостроф."
                level = "ERROR"
            else:
                msg = "Синтаксическая ошибка в коде."
                level = "ERROR"
        elif "module not found" in line_lower or "importerror" in line_lower:
            msg = "Отсутствует модуль или ошибка импорта."
            level = "ERROR"
        elif "deprecated" in line_lower:
            msg = "Используется устаревший или deprecated код."
            level = "WARNING"
        elif "warning" in line_lower:
            msg = "Предупреждение Python."
            level = "WARNING"
        elif "error" in line_lower:
            msg = "Ошибка выполнения или компиляции."
            level = "ERROR"
        else:
            msg = line.strip()
            level = "INFO"

        error_entries.append(AutoFixReportEntry(line=line_num, message=msg, level=level))

    return error_entries

def print_fix_report(reports):
    print("\n--- Подробный отчёт по ошибкам из логов ---")
    for entry in reports:
        print(entry.formatted())
    print("--- Конец отчёта ---\n")

def analyze_log_text(log_text):
    lines = log_text.splitlines()
    reports = parse_error_log(lines)
    print_fix_report(reports)
    return reports

def run_auto_fix_analysis(log_text):
    print("[AutoFix] Запуск анализа логов...")
    analyze_log_text(log_text)










# --- Обработчики Telegram ---
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Привет! Я готов к работе.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✉️ Вы сказали: {update.message.text}")

async def report_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("⛔ У вас нет доступа к этой команде.")
        return
    await update.message.reply_text("⏳ Составляю отчёт...")
    await auto_fix_from_logs()

# --- Регистрация хендлеров ---
def register_auxiliary_handlers(app):
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.add_handler(CommandHandler("report", report_handler))




import logging
import shutil
import difflib
import ast
from pathlib import Path

logger = logging.getLogger(__name__)

def fix_unclosed_syntax(code: str) -> str:
    # Твоя функция исправления незакрытых скобок и кавычек (оставляем без изменений)
    open_parens = code.count('(')
    close_parens = code.count(')')
    if open_parens > close_parens:
        code += ')' * (open_parens - close_parens)
    open_sq = code.count('[')
    close_sq = code.count(']')
    if open_sq > close_sq:
        code += ']' * (open_sq - close_sq)
    open_curly = code.count('{')
    close_curly = code.count('}')
    if open_curly > close_curly:
        code += '}' * (open_curly - close_curly)
    quote_count = code.count('"')
    if quote_count % 2 != 0:
        code += '"'
    return code






import shutil
import difflib
import ast
from pathlib import Path
import logging
from utils.fix_syntax import fix_unclosed_syntax  # функция автофикса скобок и кавычек

# Цвета ANSI
class LogColors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

class ColorFormatter(logging.Formatter):
    def format(self, record):
        color = LogColors.RESET
        if record.levelno == logging.INFO:
            color = LogColors.GREEN
        elif record.levelno == logging.WARNING:
            color = LogColors.YELLOW
        elif record.levelno == logging.ERROR:
            color = LogColors.RED
        elif record.levelno == logging.DEBUG:
            color = LogColors.CYAN
        record.msg = f"{color}{record.msg}{LogColors.RESET}"
        return super().format(record)

# Логгер с цветами
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter('%(asctime)s | %(levelname)s | %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)






import shutil
import difflib
import ast
from pathlib import Path
import logging
from utils.fix_syntax import fix_unclosed_syntax  # функция автофикса скобок и кавычек

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

async def analyze_and_fix_script(script_path: Path, log_path: Path) -> bool:
    try:
        if isinstance(script_path, str):
            script_path = Path(script_path)
        if isinstance(log_path, str):
            log_path = Path(log_path)

        if not script_path.exists():
            logger.warning(f"[WARN] 📄 Файл не найден: {script_path}")
            return False
        if not log_path.exists():
            logger.warning(f"[WARN] 🧾 Лог-файл не найден: {log_path}")
            return False

        original_code = script_path.read_text(encoding="utf-8", errors="replace")
        fixed_code = original_code
        log_content = log_path.read_text(encoding="utf-8", errors="replace")

        # --- Шаг 1: Добавляем : в async def
        if "SyntaxError: expected ':'" in log_content:
            lines = fixed_code.splitlines()
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith("async def") and not stripped.endswith(":"):
                    logger.info(f"[FIX] ✅ Добавлен ':' в строке {i + 1}")
                    lines[i] += ":"
            fixed_code = "\n".join(lines)

        # --- Шаг 2: Закрытие f-строк с нечётным числом кавычек
        if "unterminated string literal" in log_content:
            lines = fixed_code.splitlines()
            for i, line in enumerate(lines):
                if 'f"' in line or "f'" in line:
                    if line.count('"') % 2 != 0:
                        lines[i] += '"'
                        logger.info(f"[FIX] 🛠 Закрыта f-строка двойной кавычкой в строке {i + 1}")
                    elif line.count("'") % 2 != 0:
                        lines[i] += "'"
                        logger.info(f"[FIX] 🛠 Закрыта f-строка одинарной кавычкой в строке {i + 1}")
            fixed_code = "\n".join(lines)

        # --- Шаг 3: Компиляция и автоисправление скобок/кавычек
        try:
            compile(fixed_code, str(script_path), 'exec')
        except SyntaxError as e:
            logger.warning(f"[WARN] ❗ Синтаксическая ошибка: {e}")
            if e.text:
                logger.warning(f"[WARN] ➤ Строка ошибки: {e.text.strip()}")

            if "was never closed" in str(e) or "unexpected EOF" in str(e) or "unterminated string" in str(e):
                logger.info("[INFO] 🔄 Автоисправление незакрытых конструкций...")
                fixed_code2 = fix_unclosed_syntax(fixed_code)
                try:
                    compile(fixed_code2, str(script_path), 'exec')
                    backup_path = script_path.with_suffix(script_path.suffix + ".backup")
                    shutil.copy(script_path, backup_path)
                    logger.info(f"[BACKUP] 💾 Бэкап создан: {backup_path.name}")
                    script_path.write_text(fixed_code2, encoding="utf-8")
                    logger.info(f"[FIX] ✅ Незакрытые конструкции исправлены в {script_path.name}")
                    fixed_code = fixed_code2
                except SyntaxError as e2:
                    logger.error(f"[FAIL] ❌ Ошибка после автоисправления: {e2}")
                    if e2.text:
                        logger.error(f"[FAIL] ➤ Строка: {e2.text.strip()}")
                    return False
            else:
                return False

        # --- Шаг 4: AST-проверка
        try:
            ast.parse(fixed_code)
        except SyntaxError as e:
            logger.error(f"[FAIL] ❌ AST ошибка: {e}")
            if e.text:
                logger.error(f"[FAIL] ➤ Строка: {e.text.strip()}")
            return False

        # --- Шаг 5: Если есть изменения, сохраняем и выводим diff
        if fixed_code != original_code:
            script_path.write_text(fixed_code, encoding="utf-8")
            diff = difflib.unified_diff(
                original_code.splitlines(keepends=True),
                fixed_code.splitlines(keepends=True),
                fromfile=str(script_path),
                tofile=str(script_path) + " (исправлен)",
            )
            logger.info(f"[DIFF] 📋 Изменения в {script_path.name}:\n{''.join(diff)}")
            logger.info(f"[SAVE] ✅ Файл сохранён: {script_path.name}")
            return True
        else:
            logger.info("[INFO] ✅ Нет изменений — код корректен.")
            return False

    except Exception as e:
        logger.error(f"[ERROR] 🔥 Внутренняя ошибка analyze_and_fix_script: {e}")
        return False


# --- Пример использования
rita_main_path = Path("rita_main.py")
rita_log_path = Path("logs/rita_bot.log")

# Пример вызова в async:
# await analyze_and_fix_script(rita_main_path, rita_log_path)























from pathlib import Path
#from fix_code import analyze_and_fix_script  # убедись, что файл с этой функцией импортируется

async def auto_fix_from_logs():
    script_path = Path("rita_main.py")
    log_path =log_path = Path("logs/rita_bot.log")  # <-- твой лог

    logger.info("[AUTOFIX] 🔍 Анализируем rita_main.py по логам...")
    fixed = await analyze_and_fix_script(script_path, log_path)

    if fixed:
        logger.info("[✅ FIXED] rita_main.py успешно исправлен.")
    else:
        logger.info("[ℹ️] Исправлений не требуется или не удалось.")




# --- Запуск Telegram-бота ---
# --- Запуск Telegram-бота ---


from telegram.ext import Application
from telegram.error import Conflict
# --- Запуск Telegram-бота ---







from telegram.ext import Application

async def run_bot():
    try:
        # ✅ Создаём Telegram-бота с правильными параметрами
        app = (
            Application.builder()
            .token(TELEGRAM_BOT_TOKEN)
            .concurrent_updates(True)
            .close_loop(False)
            .build()
        )

        # ✅ Подключаем хендлеры
        register_auxiliary_handlers(app)

        logger.info("✅ Бот запущен и работает.")

        # ✅ Запуск фоновых задач
        asyncio.create_task(auto_fix_loop(logger))
        asyncio.create_task(auto_fix_and_restart_if_needed())
        asyncio.create_task(improvements_loop())
        start_monitoring_thread()

        # ✅ Запуск Telegram-поллинга
        await app.run_polling()

    except Exception as e:
        logger.error(f"❌ Ошибка запуска бота: {e}")







import asyncio
import sys
import logging
from telegram.ext import Application

# Предполагаем, что TELEGRAM_BOT_TOKEN и logger уже определены ранее

# --- Основная логика запуска ---
async def main_entry():
    logger.info("🚀 Старт автофикса из логов...")
    await auto_fix_from_logs()

    logger.info("💾 Выполнение резервного копирования и пуша в GitHub...")
    await auto_backup_and_push()

    logger.info("🔧 Запуск фоновых задач автофикса...")
    asyncio.create_task(auto_fix_loop(logger))
    asyncio.create_task(auto_fix_and_restart_if_needed())
    start_monitoring_thread()

    with open("rita_main.py", "r", encoding="utf-8") as f:
        your_log_text = f.read()
        run_auto_fix_analysis(your_log_text)

    logger.info("🤖 Запуск интеллектуального автоулучшения...")
    await run_intelligent_auto_improve()

    logger.info("🚀 Запуск Telegram-бота...")

    # ✅ Используем Application.builder с close_loop(False)
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).close_loop(False).build()

    # 🔄 Добавляем обработчики (если есть)
    # app.add_handler(...)  # <-- если есть хендлеры

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()
    await app.stop()
    await app.shutdown()


# --- Завершение всех задач ---
async def shutdown():
    logger.info("🛑 Завершение: отмена всех фоновых задач...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)


# --- Обёртка с защитой ---
async def main():
    log_info("🚀 Запуск скрипта диагностики RITA AI")
    if not TELEGRAM_BOT_TOKEN:
        log_error("❌ TELEGRAM_BOT_TOKEN не задан. Прекращение работы.")
        sys.exit(1)

    try:
        await main_entry()
    except Exception as e:
        logger.error(f"❌ Ошибка запуска бота: {e}")
    finally:
        await shutdown()


# --- Точка входа ---
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🚪 Завершение по Ctrl+C")
    except Exception as e:
        logger.error(f"❌ Фатальная ошибка: {e}")






