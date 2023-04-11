from aiogram import executor
import admin
from loader import *
from aiogram import types
from database import *
from expenses import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
admin.register_handlers_admin(dp)

finance = Finance()
finance.create_table()


class Captcha(StatesGroup):
    get_question = State()
    wait_answer = State()


@dp.message_handler(commands=["start"])
async def captcha_start(message: types.Message):
    await Captcha.get_question.set()
    await message.reply("10 + 5")


@dp.message_handler(state=Captcha.get_question)
async def proces_captcha(message: types.Message, state: FSMContext):
    print(message.text)
    if message.text == '15':
        print(message.text)
        async with state.proxy() as date:
            date['answer'] = message.text
            print(date)
        await message.reply("Капча пройдена, можете ввести команду /help")
        await state.finish()
    else:
        await message.reply("Вы не прошли капчу")


@dp.message_handler(commands=["help"])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот для учета финансов \n"
                         "Добавить расход: 250 такси\n"
                         "/food показывает сколько денег вы потратели на еду\n"
                         "/entertainment покзывает слолько денег вы потратили на развличения\n"
                         "/transportation покзывает слолько денег вы потратили на транспорт\n"
                         "/other покзывает слолько денег вы потратили на бесполезную вещь\n"
                         "/all_expenses все доходы")


@dp.message_handler(commands=["food"])
async def food(message: types.Message):
    user_id = message.from_user.id
    foods = finance.get_food(user_id)
    if food:
        await message.answer(f"Вы потратели на еду {foods} гривен")
    else:
        await message.answer("Вы ничего не ели гыгы, вибач")


@dp.message_handler(commands=["entertainment"])
async def food(message: types.Message):
    user_id = message.from_user.id
    entertainment = finance.get_entertainment(user_id)
    if entertainment:
        await message.answer(f"Вы потратели на развличения {entertainment} гривен")
    else:
        await message.answer("Вы целый день работали гыгы, вибач")


@dp.message_handler(commands=["transportation"])
async def food(message: types.Message):
    user_id = message.from_user.id
    transportation = finance.get_transportation(user_id)
    if transportation:
        await message.answer(f"Вы потратели на проезд {transportation} гривен")
    else:
        await message.answer("Вы опять сидели дома и никуда не ездили гыгы, вибач")


@dp.message_handler(commands=["other"])
async def food(message: types.Message):
    user_id = message.from_user.id
    other = finance.get_other(user_id)
    if other:
        await message.answer(f"Вы потратели на дичь {other} гривен, поздравляю")
    else:
        await message.answer("Вы молодець, ни на что не потратили деньги")


@dp.message_handler(commands=["all_expenses"])
async def all_expenses(message: types.Message):
    user_id = message.from_user.id
    expenses = finance.get_all_expenses(user_id)
    if expenses:
        await message.answer(f"Вы потратели вот такую суму денег {expenses} гривен")
    else:
        await message.answer("Вы ничего не потратели, бомж")


@dp.message_handler()
async def add_expense(message: types.Message):
    entert_str = ["автоматы", "парк", "кафе"]
    transportation = ["автобус", "такси", "самолет", "поезд"]
    user_id = message.from_user.id
    try:
        if 'еда' in message.text.lower():
            expense = parse_message(message.text)
            finance.add_food(expense, user_id)
            await message.answer(f"Eat add to food, amount {expense}")
        elif any(word in message.text.lower() for word in entert_str):
            expense = parse_message(message.text)
            finance.add_entertainment(expense, user_id)
            await message.answer(f"Entertainment add to entertainment, amount {expense}")
        elif any(word in message.text.lower() for word in transportation):
            expenses = parse_message(message.text)
            finance.add_transportation(expenses, user_id)
            await message.answer(f"Transportation add to transportation, amount {expenses}")
        else:
            expenses = parse_message(message.text)
            finance.add_other(expenses, user_id)
            await message.answer(f"Something add to other, amount {expenses}")
        await message.answer('Операция успешная')
    except NotCorrectMessage:
        await message.answer("Не некорректное сообщение")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
