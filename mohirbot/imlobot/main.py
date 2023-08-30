import logging
from checkWord import checkWords, has_latin
from latcyruz import toLatin
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6690698717:AAH5hkWrzIYbE7gYqDIIqdYt0VeQCuJTjp4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.reply("Xatosiz Yozamiz botiga xush kelibsiz! \n Ushbu botga yuborgan so'zingizni tekshirib beradi. Lotin va Kirill yozuvlari qo'llab-quvvatlanadi.")

@dp.message_handler(commands='help')
async def welcome(message: types.Message):
    await message.reply("Botdan foydalanish uchun o'zbek tilidagi so'zni yuboring.")

@dp.message_handler(commands='developer')
async def welcome(message: types.Message):
    await message.reply("Ushbu kod mohirdev.uz saytidagi telegram bot kursining amaliyot qismi uchun yaratildi. Bot yaratuvchisi @kamron_komil")

@dp.message_handler()
async def imlo(message: types.Message):
    xabar = checkWords(message.text)
    javob = ''
    if xabar['available']:
        javob = "\u2705"+" "+xabar['matches']
    else:
        javob = "\u274C" + message.text
        for soz in xabar['matches']:
            javob += '\n\n'+"\u2747"+" "+soz

    if has_latin(message.text):
        javob = toLatin(javob)

    await message.reply(javob)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
