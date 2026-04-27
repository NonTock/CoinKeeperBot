from config import API_KEY
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from db import add_expense, create_db, get_amount, get_resent
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Отправь трату в формате: 100 шаурма")

@dp.message(Command('getstats'))
async def get_stats_handler(message: types.Message):
    result = get_amount(message.from_user.id)
    if result is None:
        await message.answer("У вас пока не зарегистрировано трат")
    else:
        await message.answer(f" ваши траты: {result} рублей")

@dp.message(Command('getresent'))
async def get_resent_handler(message: types.Message):
    result = get_resent(message.from_user.id)
    print(result)
    if not result:
        await message.answer("У вас пока не зарегистрировано трат")
    else:
        final_mess = "Ваши последние траты:\n"
        for i, (expense, category) in enumerate(result, 1):
            final_mess += f"{i}. {expense} рублей на {category.title()}\n"
        await message.answer(final_mess)


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
    create_db()
    bot = Bot(token=API_KEY)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
