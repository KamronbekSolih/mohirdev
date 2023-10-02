from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp 

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler( msg: types.Message):
    await msg.answer_photo("https://scontent-ssn1-1.xx.fbcdn.net/v/t39.30808-6/225550490_322484322918300_8708341039336331787_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=a2f6c7&_nc_ohc=oQk7S-0wB88AX_D1rPV&_nc_ht=scontent-ssn1-1.xx&oh=00_AfD30ugx2TCN1qSvnKPs857leXdKkETmB4iTJr6_kRzj_Q&oe=6502D0FB")

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler( msg: types.Message):
    await msg.answer("Siz ovozli xabar jo'natdingiz")

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler( msg: types.Message):
    await msg.answer("Vooo qayga yo'l oldiz akasi?")

@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def video_handler( msg: types.Message):
    try:
        await msg.answer_video("https://youtu.be/GqPtk8Y0G08?si=7AX1vRNXyjfzfmLc")
    except:
        await msg.answer("Siz video jo'natdingiz.")

