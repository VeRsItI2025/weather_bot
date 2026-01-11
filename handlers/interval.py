from aiogram import Router, F
from aiogram.types import Message
from services.tasks import scheduler, send_weather_forecast
from services.storage import user_city

interval_router = Router()

@interval_router.message(F.text.in_(["Каждые 10 минут", "Каждые 3 часа", "Каждые 6 часов", "отключить рассылку"]))
async def set_interval(message: Message):
    city = user_city.get(message.chat.id)

    job_id = f"weather_{message.chat.id}"

    # Удаляем старую задачу

    if scheduler.get_job(job_id):
        scheduler.remove_job(job_id)

    if message.text == "Отключить рассылку":
        await message.answer("Рассылка отключена ❌")
        return

    if not city:
        await message.answer("Сначала выбери город ")
        return

    # Определяем интервал

    if message.text == "Каждые 10 минут":
        minutes = 10
    elif message.text == "Каждые 3 часа":
        minutes = 180
    elif message.text == "Каждые 6 часов":
        minutes = 360
    else:
        await message.answer("Неизвестный интервал. Выбери из клавиатуры.")
        return

    # Добавляем новую задачу

    scheduler.add_job(
        send_weather_forecast,
        "interval",
        minutes=minutes,
        args=[message.bot, message.chat.id, city],
        id=job_id
    )
    await message.answer(f"Рассылка прогноза для {city} настроена: {message.text}")