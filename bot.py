import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import edge_tts

TOKEN = os.getenv("TOKEN")
VOICE = "ru-RU-DmitryNeural"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет! Бот успешно переехал на сервер 24/7.")

@dp.message(F.text)
async def handle_tts(message: types.Message):
    status = await message.answer("⏳ Генерирую...")
    output_file = "voice.mp3"
    try:
        communicate = edge_tts.Communicate(message.text, VOICE)
        await communicate.save(output_file)
        
        voice_file = types.FSInputFile(output_file)
        await message.answer_voice(voice=voice_file)
        await status.delete()
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    print("🤖 Бот запущен в облаке!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
