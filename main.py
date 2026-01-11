import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start_router, weather_router
from handlers.interval import interval_router
from utils.bot_commands import set_bot_commands
from services.tasks import scheduler

BOT_TOKEN = '8416503975:AAEn6hiUxAZYExcclba2arg6aXF490vVyZY'  # твой токен

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    await set_bot_commands(bot)

    dp.include_router(start_router)
    dp.include_router(weather_router)
    dp.include_router(interval_router)

    scheduler.start()

    print("Бот запущен!")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())