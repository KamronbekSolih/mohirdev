from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp 

@dp.message_handler(Command(['til','lang']))
async def changeLanguage(message: types.Message ):
    await message.answer("O'zbek tiliga sozlandi")

@dp.message_handler(Command('mode-dev'))
async def changeLanguage(message: types.Message ):
    await message.answer("Developer mode enabled")