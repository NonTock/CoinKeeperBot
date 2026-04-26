from config import API_KEY
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from db import add_expense
dp = Dispatcher()

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Отправь трату в формате: 100 шаурма")

@dp.message()
async def answer_message(message: types.Message):
    message_text = message.text.lower()
    text = message_text.split(maxsplit=1)
    if len(text) == 1:
        await message.answer(f"{message.from_user.first_name} вы забыли указать категорию")
        return
    try:
        float(text[0])
    except ValueError:
        await message.answer(f"{text[0]} не является числом, или не подходит по формату")
        await message.answer(f"{message.from_user.first_name} введите корректное значение в формате 100[Число] шаурма[Категория]")
    else:
        add_expense(message.from_user.id, float(text[0]), text[1])
        await message.answer(f"Записал: {text[0]} руб. в категорию '{text[1]}'")

async def main():
    bot = Bot(token=API_KEY)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
