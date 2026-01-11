from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_city_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Харьков"), KeyboardButton(text="Киев")],
            [KeyboardButton(text="Одесса"), KeyboardButton(text="Львов")]

        ],
        resize_keyboard=True
    )

def get_interval_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text= "Каждые 10 минут"), KeyboardButton(text= "Каждые 3 часа")],
            [KeyboardButton(text = "Каждые 6 часов"), KeyboardButton(text= "Отключить рассылку")]
        ],
        resize_keyboard=True
    )