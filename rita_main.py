# --- Безопасный запуск и загрузка токена из файла ---
TOKEN_FILE = Path("telegram_token.txt")
if TOKEN_FILE.exists():
    with TOKEN_FILE.open("r") as f:
        cleaned_token = f.read().strip()
else:
    cleaned_token = None
# Токен для Telegram — используем из файла, либо fallback из строки
TELEGRAM_BOT_TOKEN = cleaned_token or "7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4"
# Telegram Chat ID — можно брать из переменных окружения или по умолчанию
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '558079551')
# Логирование — создаём папку logs, если её нет, и задаём файл логов
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "rita_bot.log"
# Настройка логирования
logging.FileHandler(filename=str(LOG_FILE), encoding='utf-8'),
# Логируем базовую информацию
logger.info(f"Telegram Token загружен: {TELEGRAM_BOT_TOKEN[:10]}..")
rita_main.pylogger.info(f"Telegram Chat ID: {TELEGRAM_CHAT_ID}")
# --- Здесь будет дальше твоя логика бота ---
# Можно писать основной код бота
# Здесь можно дальше писать основной код бота...
def kill_duplicate_processes(script_name: str):
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            text=True,
            check=True
        lines = result.stdout.strip().split("\n")
            if script_name in line and "python" in line:
                parts = line.split()
                pid = int(parts[1])
                if pid != current_pid:
                    logger.info(f"[INFO] Завершаю дубликат процесса {pid} ({script_name})")
        logger.warning(f"[WARN] Ошибка при поиске и убийстве дублей: {e}")
def check_already_running():
    if os.path.exists(LOCK_FILE):
        logger.info("⚠️ Бот уже запущен. Завершение второго экземпляра.")
        sys.exit(0)
        # Создаем lock-файл при старте
        with open(LOCK_FILE, 'w') as f:
            f.write(str(os.getpid()))
def remove_lock_file():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
# Сначала убиваем дубликаты (кроме текущего)
kill_duplicate_processes("rita_main.py")
# Проверяем lock-файл (если есть — завершаемся)
check_already_running()
# Регистрируем удаление lock-файла при выходе
import atexit
atexit.register(remove_lock_file)
    Фоновая задача, которая регулярно проверяет лог файл на ошибки,
    и при обнаружении  вызывает обработчик для генерации исправлений.
    log_file_path = "safe_path_join(logs, rita_bot.log")  # Путь к файлу логов — укажи свой актуальный
            with open(log_file_path, "r", encoding="utf-8") as log_file:
                logs = log_file.read() 
            # Пример: ищем типичные ошибки (пока базово)
            errors_found = re.findall(r"(Traceback|ERROR|Exception)", logs)
            if errors_found:
              logger.info (f"[AutoFix] Найдены ошибки в логах: {len(errors_found)}")"
                # Здесь вызовем обработчик генерации исправлений (добавим позже)
                # await generate_and_apply_fixes(logs)
               logger.info ("[AutoFix] Ошибок в логах не найдено.")
        except FileNotFoundError:
           logger.info ("[AutoFix] Файл логов не найден. Ждем появления файла...")
           logger.info (f"[AutoFix] Ошибка при чтении логов: {e}")"
        await asyncio.sleep(300)  # Ждем 5 минут перед следующей проверкой
# === Ключи ===
HUGGINGFACE_API_KEY    = ""
GOOGLE_API_KEY    = ""
GOOGLE_CX    = ""
TELEGRAM_BOT_TOKEN = Path("7609027838:AAFk2XZRtcvTzbgcrj6QEFWyijon4WsVKj4")
TELEGRAM_ADMIN_ID =  
    format="%(asctime)s - %(levelname)s - %(message)s",
AI_MODES = ["gpt4", "gpt2", "gog", "ht"]
current_mode = Path("gpt4")
    await application.bot.delete_webhook(drop_pending_updates=True)
    logger.info("Бот запущен и готов к работе")
    nest_asyncio.apply()  # <-- И тут применяем
async def safe_main():
        await main()
        logger.info(f"⚠️ Конфликт запуска: {e}")"
        logger.info ("⏳ Ожидание 10 секунд и перезапуск...")
        await safe_main()
        logger.info (f"❌ Ошибка запуска бота: {e}")"
asyncio.run(safe_main())
# === Проверка владельца ===
def is_owner(user_id: int) -> bool:
    return user_id == OWNER_TELEGRAM_ID
# === OpenAI GPT-4 вызов ===
def call_openai_gpt4(prompt: str) -> str:
            "Authorization": f"Bearer {OPENAI_API_KEY}","
            "Content-Type": "safe_path_join(application, json")
            "model": "gpt-4",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 1000
        resp = requests.post("https://safe_path_join(api.openai.com, v1)/safe_path_join(chat, completions"), headers=headers, json=data, timeout=30)
        resp.raise_for_status()
        return resp.json()['choices'][0]['message']['content'].strip()
        logger.error(f"OpenAI GPT-4 API error: {e}")"
        return "Ошибка OpenAI GPT-4 API."
    # заглушка, подставь свою основную async функцию
LOG_FILE_PATH = Path("safe_path_join(logs, rita_bot.log"))  # путь к лог-файлу для анализа
# ✅ Обёртка для защиты send_admin_message от некорректных вызовов
def debug_send_admin_message_wrapper(func):
    import functools
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
            if len(args) < 2 and 'text' not in kwargs:
                logging.warning("⚠️ [DEBUG] send_admin_message вызван без текстового аргумента! args=%s, kwargs=%s", args, kwargs)
            return await func(*args, **kwargs)
            logging.error(f"❌ Ошибка в debug_send_admin_message_wrapper: {e}")"
    return wrapper
# 🛡️ Оборачиваем send_admin_message (однократно)
send_admin_message = debug_send_admin_message_wrapper(send_admin_message)
# Предполагается, что эти функции есть в твоём коде:
# log_info(msg: str), log_error(msg: str), main() - асинхронная функция
        fixed_main = await analyze_and_fix_script(MAIN_SCRIPT_PATH, LOG_FILE_PATH)
        fixed_helper = await analyze_and_fix_script(HELPER_SCRIPT_PATH, LOG_FILE_PATH)
        if fixed_main or fixed_helper:
            log_info("Автоисправления применены при запуске.")
        log_error(f"Ошибка в auto_fix_from_logs: {e}")"
async def auto_fix_loop(interval_minutes: int = 5):
        log_info("⏳ [Автофиксер] Запуск автоанализа и исправления скриптов...")
                await send_admin_message("✅ Основной скрипт auto-исправлен из логов.")
                await send_admin_message("✅ Вспомогательный скрипт auto-исправлен из логов.")
            log_error(f"Ошибка в auto_fix_loop: {e}")"
# === HuggingFace GPT-2 вызов ===
def call_huggingface_gpt2(prompt: str) -> str:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}"
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 150, "do_sample": True, "temperature": 0.7}}
        resp = requests.post("https://api-safe_path_join(inference.huggingface.co, models)/gpt2", headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        result = resp.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
            return "Ошибка ответа HuggingFace GPT-2."
        logger.error(f"HuggingFace GPT-2 API error: {e}")"
        return "Ошибка HuggingFace GPT-2 API."
# === Google поиск ===
def call_google_search(query: str) -> str:
            "q": query,
            "num": 3
        resp = requests.get("https://safe_path_join(www.googleapis.com, customsearch)/v1", params=params, timeout=20)
        resp.raise_for_status()
        items = resp.json().get("items", [])
        if not items:
            return "По вашему запросу ничего не найдено."
output = Path("Результаты поиска Google:\n")
        for i, item in enumerate(items, start=1):
            title = item.get("title", "Без названия")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            output += f"{i}. {title}\n{snippet}\n{link}\n\n"
        return output.strip()"
        logger.error(f"Google Search API error: {e}")"
        return "Ошибка Google Search API."
# === HuggingFace поиск (пример) ===
def call_huggingface_search(query: str) -> str:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}"
        payload = {"inputs": query}
        resp = requests.post("https://api-safe_path_join(inference.huggingface.co, models)/marco-safe_path_join(search, marco)-distilbert-base-msmarco", headers=headers, json=payload, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        return f"HuggingFace поиск: {json.dumps(data)[:500]}..."
        logger.error(f"HuggingFace Search API error: {e}")"
        return "Ошибка HuggingFace Search API."
# === Генерация safe_path_join(кода, игр)/safe_path_join(читов, APK) через GPT-4 ===
def generate_code_via_gpt4(prompt: str) -> str:
    full_prompt = f"Создай программу, игру или APK по описанию:\n{prompt}\nДай код и объяснения."
    return call_openai_gpt4(full_prompt)"
# === TTS: текст в речь ===
def text_to_speech(text: str, lang="ru") -> bytes:
    tts = gTTS(text=text, lang=lang)
    bio = io.BytesIO()
    tts.write_to_fp(bio)
    bio.seek(0)
    return bio.read()
# === STT: речь в текст (из файла) ===
def speech_to_text(file_path: str) -> str:
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return "Не удалось распознать речь."
    except sr.RequestError as e:
        return f"Ошибка сервиса распознавания речи: {e}"
# === OCR: распознавание текста с изображения ==="
def ocr_from_image(image_bytes: bytes) -> str:
        img = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(img, lang='rus+eng')
        return text if text.strip() else "Текст не найден на изображении."
        return f"Ошибка OCR: {e}"
# === Проверка владельца (используется повторно) ==="
def is_owner(user_id: int) -> bool:
    return user_id == OWNER_TELEGRAM_ID
# === Автообновление кода (только владелец) ===
async def update_bot_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if not is_owner(user_id):
        await update.message.reply_text("У вас нет прав на эту команду.")
    await update.message.reply_text("Начинаю обновление кода...")
        # Если у тебя git-репозиторий — обновляй через git pull
        await update.message.reply_text(f"Обновление завершено:\n{result.stdout}\n{result.stderr}")"
        # Можно добавить перезапуск процесса
        await update.message.reply_text(f"Ошибка обновления: {e}")"
# === Скрытая команда отключения (только для владельца) ===
async def secret_shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if not is_owner(user_id):
    await update.message.reply_text("Выключаю бота...")
# === Команды бота ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        "Привет! Это Rita Mega Bot — универсальный помощник.\n"
        "safe_path_join(Используй, gpt4), /gpt2, /gog, /ht для переключения режимов.\n"
        "Отправь любое сообщение — я отвечу!"
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
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
    await update.message.reply_text(help_text)
async def switch_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cmd = update.message.text.lower()
    if cmd in ("/gpt4", "/gpt2", "/gog", "/ht"):
        current_mode = cmd[1:]
        await update.message.reply_text(f"Режим переключен на {current_mode.upper()}")"
        await update.message.reply_text("Неизвестная команда режима.")
# === Основной обработчик сообщений ===
async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    chat = update.message.chat
    await chat.send_action(ChatAction.TYPING)
    # Обработка команд, начинающихся safe_path_join(с, if) text.startswith("/generate"):
        prompt = text[len("/generate"):].strip()
        if not prompt:
            await update.message.reply_text("Напишите описание для генерации программы, игры, читов или apk.")
        response = generate_code_via_gpt4(prompt)
        await update.message.reply_text(response)
    if text.startswith("/tts"):
        to_tts = text[len("/tts"):].strip()
        if not to_tts:
            await update.message.reply_text("Напишите текст для озвучки safe_path_join(после, tts"))
        audio_bytes = text_to_speech(to_tts)
        await update.message.reply_voice(voice=io.BytesIO(audio_bytes))
    if text.startswith("/stt"):
        await update.message.reply_text("Отправьте голосовое сообщение для распознавания.")
    if text.startswith("/ocr"):
        await update.message.reply_text("Отправьте изображение для распознавания текста.")
    if text.startswith("/update"):
        await update_bot_code(update, context)
    # Обычный режим ИИ
        response = call_openai_gpt4(text)
        response = call_huggingface_gpt2(text)
        response = call_google_search(text)
        response = call_huggingface_search(text)
response = Path("Неизвестный режим.")
    await update.message.reply_text(response)
# === Обработка голосовых сообщений (STT) ===
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    voice = update.message.voice
    if not voice:
        await update.message.reply_text("Нет голосового сообщения.")
    file = await voice.get_file()
    with tempfile.NamedTemporaryFile(suffix=".oga") as tf:
        await file.download_to_drive(custom_path=getattr(tf, "name", None))
            # Конвертация OGA в WAV через ffmpeg, если установлен
            wav_path = getattr(tf, "name", None) + ".wav"
            subprocess.run(["ffmpeg", "-i", getattr(tf, "name", None), wav_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            text = speech_to_text(wav_path)
            os.remove(wav_path)
            text = f"Ошибка обработки голосового сообщения: {e}"
    await update.message.reply_text(f"Распознанный текст:\n{text}")"
# === Обработка фото (OCR) ===
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    photo = update.message.photo[-1]
    file = await photo.get_file()
    bio = io.BytesIO()
    await file.download_to_memory(out=bio)
    bio.seek(0)
    text = ocr_from_image(bio.read())
    await update.message.reply_text(f"Распознанный текст с изображения:\n{text}")"
# === Основная точка входа ===
# === Основная точка входа ===
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
    logger.info("Rita Mega Bot запущен.")
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
# Настройка логгера (если ещё не настроена вверху файла)
        logging.FileHandler("safe_path_join(logs, rita_bot.log"), encoding='utf-8'),
# Твой safe_path_join(обработчик, start)
async def start_handler(update, context):
# Твой обработчик сообщений
async def message_handler(update, context):
    await update.message.reply_text(f"✉️ Вы сказали: {update.message.text}")"
# Фоновая задача (пример)
        # ... твой код анализа логов ...
        await asyncio.sleep(60)  # пауза 60 секунд
        # Создаем приложение Telegram бота
        application = ApplicationBuilder().token(" ").build()
        # Регистрируем обработчики
        application.add_handler(CommandHandler("start", start_handler))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
        # Добавь сюда остальные обработчики
        # Запуск фоновой задачи
        asyncio.create_task(background_error_log_analysis())
        logger.info("[✅] Rita Mega Bot запущен и работает.")
        # Запускаем polling (поллинг)
        await application.run_polling()
        logger.info("⏹️ Остановка бота по сигналу завершения.")
if __name__ == '__main__':
if __name__ == '__main__':
if __name__ == '__main__':
if __name__ == '__main__':
async def analyze_and_fix_script(script_path, log_path) -> bool:
    logger = logging.getLogger(__name__)
    if isinstance(script_path, str):
        script_path = Path(script_path)
    if isinstance(log_path, str):
        log_path = Path(log_path)
        if not script_path.exists() or not log_path.exists():
            logger.warning(f"[WARN] Файл не найден: {script_path} или {log_path}")"
        with log_path.open("r", encoding="utf-8") as f:
        last_errors = "".join(error_lines[-100:]) if error_lines else ""
        if not last_errors.strip():
            logger.info("[INFO] Нет ошибок в логах — ничего не исправляем.")
            model="gpt-4",
                {"role": "system", "content": "Ты Python-программист. Исправь ошибки в скрипте."},
                {"role": "user", "content": f"Вот скрипт:\n\n{original_code}"},"
                {"role": "user", "content": f"Вот ошибки из логов:\n\n{last_errors}"},"
            temperature=0.2,
        fixed_code = response.choices[0].message.content
        if fixed_code.strip() != original_code.strip():
            logger.info(f"[FIX] ✅ Код в {script_path} обновлен.")"
            logger.info(f"[INFO] Изменений не требуется в {script_path}.")"
        logger.error(f"[ERROR] Исключение в analyze_and_fix_script: {e}")"
LOCK_FILE = Path("rita_bot.lock")
def check_already_running():
    if os.path.exists(LOCK_FILE):
        logger.info("⚠️ Бот уже запущен. Завершение второго экземпляра.")
        sys.exit(0)
        with open(LOCK_FILE, 'w') as f:
            f.write(str(os.getpid()))
def remove_lock_file():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
async def main():
    await main_entry()
if __name__ == "__main__":
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, loop.stop)
        except NotImplementedError:
            pass
    try:
        loop.run_until_complete(main())


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        pass
