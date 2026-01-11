from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.keyboard import get_city_keyboard

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Привет! Выбери город из списка или напиши свой 🌍",
        reply_markup=get_city_keyboard()
    )