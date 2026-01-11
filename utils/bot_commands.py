from aiogram import Bot
from aiogram.types import BotCommand
from aiogram import Router

router=Router()

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начать работу'),
        BotCommand(command='weather', description="Погода")

    ]
    await bot.set_my_commands(commands)