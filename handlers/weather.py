from aiogram import Router, F
from aiogram.types import Message

from keyboards.keyboard import get_interval_keyboard
from services.weather_api import get_weather
from services.storage import user_city

weather_router = Router()

INTERVAL_TEXTS = {
    "Каждые 10 минут",
    "Каждые 3 часа",
    "Каждые 6 часов",
    "Отключение рассылки",
}

@weather_router.message(
    F.text
    & ~F.text.startswith("/")
    & ~F.text.in_(INTERVAL_TEXTS)
)
async def weather(message: Message):
    city = message.text.strip()
    forecast = get_weather(city)

    if forecast == "Не удалось найти город":
        await message.answer("Не удалось найти город. Попробуй ещё раз 🧭")
        return

    await message.answer(forecast)

    user_city[message.chat.id] = city

    # Предлагаем выбрать интервал
    await message.answer("Выбери интервал рассылки ⏱", reply_markup=get_interval_keyboard())
