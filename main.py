from config import API_KEY
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
dp = Dispatcher()

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Отправь трату в формате: 100 шаурма")

@dp.message()
async def answer_message(message: types.Message):
    message_text = message.text.lower()
    text = message_text.split(maxsplit=1)
    try:
        float(text[0])
    except ValueError:
        await message.answer(f"{text[0]} не является числом, или не подходит по формату")
        await message.answer(f"{message.from_user.first_name} введи корректное значение в формате 100[Число] шаурма[Категория]")
    else:
        await message.answer(f"Записал: {text[0]} руб. в категорию '{text[1]}'")

async def main():
    bot = Bot(token=API_KEY)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
