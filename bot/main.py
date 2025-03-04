import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))

import asyncio

from aiogram import Dispatcher, Bot

from bot.database import init_db
from bot.config import BOT_TOKEN
from handlers.start import starter

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
dp.include_router(starter)

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())