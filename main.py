from aiogram import executor
from loader import *
from aiogram import types
from database import *
from exceptions import *
from expenses import *


finance = Finance()
finance.create_table()

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот для учета финансов \n"
                         "Добавить расход: 250 такси\n")


@dp.message_handler()
async def add_expense(message: types.Message):
    entert_str = ["автоматы", "парк", "кафе"]
    transportation = ["автобус", "такси", "самолет", "поезд"]

    if 'Еда' in message.text.lower():
        print('find eat')
        expense = parse_message(message.text)
        finance.add_food(expense)
        await message.answer(f"Eet add to food, amount {expense}")
    elif any(word in message.text.lower() for word in entert_str):
        expense = parse_message(message.text)
        finance.add_entertainment(expense)
        await message.answer(f"Entertainment add to entertainment, amount {expense}")
    elif any(word in message.text.lower() for word in transportation):
        expenses = parse_message(message.text)
        finance.add_transportation(expenses)
        await message.answer(f"Transportation add to transportation, amount {expenses}")
    else:
        expenses = parse_message(message.text)
        finance.add_other(expenses)
        await message.answer(f"Something add to other, amount {expenses}")

    await message.answer('operation secsesfull')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)