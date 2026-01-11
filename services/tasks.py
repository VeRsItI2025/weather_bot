from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services.weather_api import get_weather

scheduler = AsyncIOScheduler()

async def send_weather_forecast(bot, chat_id: int, city: str):
    forecast = get_weather(city)
    await bot.send_message(chat_id, f"Прогноз погоды для {city}:\n{forecast}")