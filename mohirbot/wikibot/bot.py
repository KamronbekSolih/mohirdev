"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wiki
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6667411558:AAGR0aBN5BXH8aTDDCgF3CA-wxNcz--bn-M'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum! Wikipediya botiga xush kelibsiz!")



@dp.message_handler()
async def FindWiki(message: types.Message):
    
    try:
        await message.answer(wiki.sorov("uz",message))
    except:
        await message.answer("Siz qidirgan maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)