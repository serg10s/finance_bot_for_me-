from aiogram import executor
from loader import *
from aiogram import types
from database import *
from exceptions import NotCorrectMessage
from expenses import *


finance = Finance()
finance.create_table()


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот для учета финансов \n"
                         "Добавить расход: 250 такси\n"
                         "/food показывает сколько денег вы потратели на еду\n"
                         "/entertainment покзывает слолько денег вы потратили на развличения\n"
                         "/transportation покзывает слолько денег вы потратили на транспорт\n"
                         "/other покзывает слолько денег вы потратили бесполезную вещь")


@dp.message_handler(commands=["food"])
async def food(message: types.Message):
    food = finance.get_food()
    if food:
        await message.answer(f"Вы потратели на еду {food} гривен")
    else:
        await message.answer("Вы ничего не ели гыгы, вибач")


@dp.message_handler(commands=["entertainment"])
async def food(message: types.Message):
    entertainment = finance.get_entertainment()
    if entertainment:
        await message.answer(f"Вы потратели на развличения {entertainment} гривен")
    else:
        await message.answer("Вы целый день работали гыгы, вибач")


@dp.message_handler(commands=["transportation"])
async def food(message: types.Message):
    transportation = finance.get_transportation()
    if transportation:
        await message.answer(f"Вы потратели на проезд {transportation} гривен")
    else:
        await message.answer("Вы опять сидели дома и никуда не ездили гыгы, вибач")


@dp.message_handler(commands=["other"])
async def food(message: types.Message):
    other = finance.get_other()
    if food:
        await message.answer(f"Вы потратели на дичь {other} гривен, поздравляю")
    else:
        await message.answer("Вы молодець, ни на что не потратили деньги")


@dp.message_handler()
async def add_expense(message: types.Message):
    entert_str = ["автоматы", "парк", "кафе"]
    transportation = ["автобус", "такси", "самолет", "поезд"]
    try:
        if 'еда' in message.text.lower():
            expense = parse_message(message.text)
            finance.add_food(str(expense))
            await message.answer(f"Eat add to food, amount {expense}")
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
        await message.answer('Операция успешная')
    except NotCorrectMessage:
        await message.answer("Не некорректное сообщение")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
