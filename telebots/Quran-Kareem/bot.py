import logging
from random import randint 
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6673820815:AAG3R6IebJn_HIHfruZ9959g_cqTCYll3Cg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def javob(message: types.Message):
    if ":" in message.text:
        manzil = list(message.text.replace(":"," ").split())
        sura = manzil[0]
        oyat = manzil[1]
        ayat = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-quran-la4/{sura}/{oyat}.json").json()['text']
        tafsir = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json").json()['text']
        qiroat = requests.get(f"http://api.alquran.cloud/v1/ayah/{sura}:{oyat}/ar.alafasy").json()['data']['audio']
        javob = f"<b>{ayat.capitalize()}</b>, \n\n {tafsir.capitalize()}"
        await message.answer_audio(qiroat)
        await message.answer(javob,'HTML')
        
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)