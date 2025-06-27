

import os
import sys
import re
import io
import json
import asyncio
import tempfile
import subprocess
import logging
from pathlib import Path

import requests
from gtts import gTTS
import speech_recognition as sr
from PIL import Image
import pytesseract

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import nest_asyncio


# --- Конфигурация ---


import os
from pathlib import Path
from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()

LOCK_FILE = "/data/data/com.termux/files/usr/tmp/rita_main.lock"
MAIN_SCRIPT_PATH = Path("rita_main.py")
HELPER_SCRIPT_PATH = Path("check_bot_diagnostics.py")
LOG_FILE_PATH = Path("rita_bot.log")  # Лог пишется в rita_bot.log

# Ключи API из переменных окружения
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_TELEGRAM_ID = int(os.getenv("OWNER_TELEGRAM_ID", "0"))

AI_MODES = ["gpt4", "gpt2", "gog", "ht"]
current_mode = "gpt4"




# --- Логирование ---

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("rita_bot.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# --- Утилиты ---

def check_already_running():
    if os.path.exists(LOCK_FILE):
        logger.info("⚠️ Бот уже запущен. Завершение второго экземпляра.")
        sys.exit(0)
    else:
        with open(LOCK_FILE, 'w') as f:
            f.write(str(os.getpid()))

def remove_lock_file():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)

def kill_duplicate_processes(script_name: str):
    current_pid = os.getpid()
    try:
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().split("\n")
        for line in lines:
            if script_name in line and "python" in line:
                parts = line.split()
                pid = int(parts[1])
                if pid != current_pid:
                    logger.info(f"[INFO] Завершаю дубликат процесса {pid} ({script_name})")
                    os.kill(pid, 15)  # SIGTERM
    except Exception as e:
        logger.warning(f"[WARN] Ошибка при поиске и убийстве дублей: {e}")

def is_owner(user_id: int) -> bool:
    return user_id == OWNER_TELEGRAM_ID

# --- OpenAI GPT-4 API вызов ---

def call_openai_gpt4(prompt: str) -> str:
    try:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 1000
        }
        resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data, timeout=30)
        resp.raise_for_status()
        return resp.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        logger.error(f"OpenAI GPT-4 API error: {e}")
        return "Ошибка OpenAI GPT-4 API."

# --- HuggingFace GPT-2 API вызов ---

def call_huggingface_gpt2(prompt: str) -> str:
    try:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 150, "do_sample": True, "temperature": 0.7}}
        resp = requests.post("https://api-inference.huggingface.co/models/gpt2", headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        result = resp.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return "Ошибка ответа HuggingFace GPT-2."
    except Exception as e:
        logger.error(f"HuggingFace GPT-2 API error: {e}")
        return "Ошибка HuggingFace GPT-2 API."

# --- Google поиск ---

def call_google_search(query: str) -> str:
    try:
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CX,
            "q": query,
            "num": 3
        }
        resp = requests.get("https://www.googleapis.com/customsearch/v1", params=params, timeout=20)
        resp.raise_for_status()
        items = resp.json().get("items", [])
        if not items:
            return "По вашему запросу ничего не найдено."
        output = "Результаты поиска Google:\n"
        for i, item in enumerate(items, start=1):
            title = item.get("title", "Без названия")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            output += f"{i}. {title}\n{snippet}\n{link}\n\n"
        return output.strip()
    except Exception as e:
        logger.error(f"Google Search API error: {e}")
        return "Ошибка Google Search API."

# --- HuggingFace поиск ---

def call_huggingface_search(query: str) -> str:
    try:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        payload = {"inputs": query}
        resp = requests.post("https://api-inference.huggingface.co/models/marco-search/marco-distilbert-base-msmarco", headers=headers, json=payload, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        return f"HuggingFace поиск: {json.dumps(data)[:500]}..."
    except Exception as e:
        logger.error(f"HuggingFace Search API error: {e}")
        return "Ошибка HuggingFace Search API."

# --- Генерация кода через GPT-4 ---

def generate_code_via_gpt4(prompt: str) -> str:
    full_prompt = f"Создай программу, игру или APK по описанию:\n{prompt}\nДай код и объяснения."
    return call_openai_gpt4(full_prompt)

# --- TTS: текст в речь ---

def text_to_speech(text: str, lang="ru") -> bytes:
    tts = gTTS(text=text, lang=lang)
    bio = io.BytesIO()
    tts.write_to_fp(bio)
    bio.seek(0)
    return bio.read()

# --- STT: речь в текст ---

def speech_to_text(file_path: str) -> str:
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return "Не удалось распознать речь."
    except sr.RequestError as e:
        return f"Ошибка сервиса распознавания речи: {e}"

# --- OCR: распознавание текста с изображения ---

def ocr_from_image(image_bytes: bytes) -> str:
    try:
        img = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(img, lang='rus+eng')
        return text if text.strip() else "Текст не найден на изображении."
    except Exception as e:
        return f"Ошибка OCR: {e}"

# --- Автообновление кода бота ---

async def update_bot_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if not is_owner(user_id):
        await update.message.reply_text("У вас нет прав на эту команду.")
        return
    await update.message.reply_text("Начинаю обновление кода...")
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        await update.message.reply_text(f"Обновление завершено:\n{result.stdout}\n{result.stderr}")
        # Перезапуск бота можно добавить здесь, если нужно
    except Exception as e:
        await update.message.reply_text(f"Ошибка обновления: {e}")

# --- Скрытая команда выключения ---

async def secret_shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if not is_owner(user_id):
        return
    await update.message.reply_text("Выключаю бота...")
    sys.exit(0)

# --- Обработчики команд ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Это Rita Mega Bot — универсальный помощник.\n"
        "Используй /gpt4, /gpt2, /gog, /ht для переключения режимов.\n"
        "Отправь любое сообщение — я отвечу!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Доступные команды:\n"
        "/start - Запуск бота\n"
        "/help - Справка\n"
        "/gpt4 - Режим OpenAI GPT-4\n"
        "/gpt2 - Режим HuggingFace GPT-2\n"
        "/gog - Режим Google поиск\n"
        "/ht - Режим HuggingFace поиск\n"
        "/generate - Генерация программ, игр, читов, apk (через GPT)\n"
        "/tts - Голосовой вывод (текст в речь)\n"
        "/stt - Голосовой ввод (речь в текст)\n"
        "/ocr - Распознавание текста с фото\n"
        "/update - Автообновление кода (только владелец)\n"
    )
    await update.message.reply_text(help_text)

async def switch_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_mode
    cmd = update.message.text.lower()
    if cmd in ("/gpt4", "/gpt2", "/gog", "/ht"):
        current_mode = cmd[1:]
        await update.message.reply_text(f"Режим переключен на {current_mode.upper()}")
    else:
        await update.message.reply_text("Неизвестная команда режима.")

# --- Основной обработчик сообщений ---



async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text or ""
    chat = update.message.chat

    await chat.send_action(ChatAction.TYPING)

    # Обработка команд, начинающихся с /
    if text.startswith("/generate"):
        prompt = text[len("/generate"):].strip()
        if not prompt:
            await update.message.reply_text("Напишите описание для генерации программы, игры, читов или apk.")
            return
        response = generate_code_via_gpt4(prompt)
        await update.message.reply_text(response)
        return

    if text.startswith("/tts"):
        to_tts = text[len("/tts"):].strip()
        if not to_tts:
            await update.message.reply_text("Напишите текст для озвучки после /tts")
            return
        audio_bytes = text_to_speech(to_tts)
        await update.message.reply_voice(voice=io.BytesIO(audio_bytes))
        return

    if text.startswith("/stt"):
        await update.message.reply_text("Отправьте голосовое сообщение для распознавания.")
        return

    if text.startswith("/ocr"):
        await update.message.reply_text("Отправьте изображение для распознавания текста.")
        return

    if text.startswith("/update"):
        await update_bot_code(update, context)
        return

    # Обычный режим ИИ
    global current_mode
    if current_mode == "gpt4":
        response = call_openai_gpt4(text)
    elif current_mode == "gpt2":
        response = call_huggingface_gpt2(text)
    elif current_mode == "gog":
        response = call_google_search(text)
    elif current_mode == "ht":
        response = call_huggingface_search(text)
    else:
        response = "Неизвестный режим."

    await update.message.reply_text(response)








async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    voice = update.message.voice
    if not voice:
        await update.message.reply_text("Нет голосового сообщения.")
        return
    file = await voice.get_file()
    with tempfile.NamedTemporaryFile(suffix=".oga") as tf:
        await file.download_to_drive(custom_path=tf.name)
        try:
            # Конвертация OGA в WAV через ffmpeg (если установлен)
            wav_path = tf.name + ".wav"
            subprocess.run(
                ["ffmpeg", "-i", tf.name, wav_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            text = speech_to_text(wav_path)
            os.remove(wav_path)
        except Exception as e:
            text = f"Ошибка обработки голосового сообщения: {e}"
    await update.message.reply_text(f"Распознанный текст:\n{text}")
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    photo = update.message.photo[-1]  # самое большое разрешение
    file = await photo.get_file()
    bio = io.BytesIO()
    await file.download_to_memory(out=bio)
    bio.seek(0)
    text = ocr_from_image(bio.read())
    await update.message.reply_text(f"Распознанный текст с изображения:\n{text}")











async def analyze_and_fix_script(script_path, log_path) -> bool:
    import openai
    from pathlib import Path

    if isinstance(script_path, str):
        script_path = Path(script_path)
    if isinstance(log_path, str):
        log_path = Path(log_path)

    try:
        if not script_path.exists() or not log_path.exists():
            logger.warning(f"[WARN] Файл не найден: {script_path} или {log_path}")
            return False

        with log_path.open("r", encoding="utf-8") as f:
            lines = f.readlines()

        error_lines = [line for line in lines if "[ERROR]" in line or "Traceback" in line]
        last_errors = "".join(error_lines[-100:]) if error_lines else ""

        if not last_errors.strip():
            logger.info("[INFO] Нет ошибок в логах — ничего не исправляем.")
            return False

        original_code = script_path.read_text(encoding="utf-8")

        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",  # заменили модель на доступную всем
            messages=[
                {"role": "system", "content": "Ты Python-программист. Исправь ошибки в скрипте."},
                {"role": "user", "content": f"Вот скрипт:\n\n{original_code}"},
                {"role": "user", "content": f"Вот ошибки из логов:\n\n{last_errors}"},
            ],
            temperature=0.2,
        )

        fixed_code = response.choices[0].message.content

        if fixed_code.strip() != original_code.strip():
            script_path.write_text(fixed_code, encoding="utf-8")
            logger.info(f"[FIX] ✅ Код в {script_path} обновлен.")
            return True
        else:
            logger.info(f"[INFO] Изменений не требуется в {script_path}.")
            return False

    except Exception as e:
        logger.error(f"[ERROR] Исключение в analyze_and_fix_script: {e}")
        return False
































async def auto_fix_loop(interval_minutes: int = 5):
    while True:
        logger.info("⏳ [Автофиксер] Запуск автоанализа и исправления скриптов...")
        try:
            main_updated = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
            helper_updated = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)

            if main_updated:
                # Тут можно уведомить администратора через телегу, например
                logger.info("✅ Основной скрипт auto-исправлен из логов.")

            if helper_updated:
                logger.info("✅ Вспомогательный скрипт auto-исправлен из логов.")

        except Exception as e:
            logger.error(f"Ошибка в auto_fix_loop: {e}")

        await asyncio.sleep(interval_minutes * 60)
async def main():
    # Убиваем дубликаты скриптов, если есть
    kill_duplicate_processes("rita_main.py")

    # Проверяем, что бот уже не запущен
    check_already_running()

    # Регистрируем удаление lock файла при выходе
    import atexit
    atexit.register(remove_lock_file)

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("gpt4", switch_mode))
    app.add_handler(CommandHandler("gpt2", switch_mode))
    app.add_handler(CommandHandler("gog", switch_mode))
    app.add_handler(CommandHandler("ht", switch_mode))
    app.add_handler(CommandHandler("update", update_bot_code))

    # Обработчики сообщений
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_all_messages))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Запуск автофикса в фоне
    asyncio.create_task(auto_fix_loop())

    logger.info("Rita Mega Bot запущен и готов к работе")
    await app.run_polling()

if __name__ == "__main__":
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("⏹️ Остановка бота по сигналу завершения.")
    finally:
        remove_lock_file()




if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass