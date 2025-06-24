# fix_token_issue.py
import os
import sys
import asyncio
from dotenv import load_dotenv
from telegram import Bot

print("🛠️ Запуск fix_token_issue.py")

load_dotenv()

raw_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
clean_token = raw_token.strip().replace(" ", "").replace("\n", "")

print(f"🔍 Загружаем переменные из .env...")
print(f"[DEBUG] Raw token: {repr(raw_token)}")
print(f"[DEBUG] Cleaned token: {repr(clean_token)}")

if not clean_token:
    print("❌ TELEGRAM_BOT_TOKEN не найден или пустой")
    sys.exit(1)

async def check_token(token):
    try:
        bot = Bot(token=token)
        me = await bot.get_me()
        print(f"✅ Токен действителен. Бот: @{me.username}")
        with open(".token_clean", "w") as f:
            f.write(token)
    except Exception as e:
        print(f"❌ Ошибка токена: {e}")
        sys.exit(1)

asyncio.run(check_token(clean_token))
