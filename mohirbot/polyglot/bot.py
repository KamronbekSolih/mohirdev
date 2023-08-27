import logging
from googletrans import Translator
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6638614472:AAHeHcsoHjKZwebttmrPp6lwbMEMr3UoFJY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler()
async def tarjimon(message: types.Message):
    word = message.text
    tilmoch = Translator()

    uzbekcha = tilmoch.translate(word,'uz','en').text
    ruscha = tilmoch.translate(word,'ru','en').text
    koreyscha = tilmoch.translate(word, 'ko','en').text
    nemischa = tilmoch.translate(word,'de','en').text

    tarjima = f"*O'zbekcha:* _{uzbekcha}_ \n\n*На русском:* _{ruscha}_ \n\n*Deutsch:* _{nemischa}_ \n\n*한국:* _{koreyscha}_"


    await message.answer(tarjima,"Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
