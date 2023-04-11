from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from database import *


finance = Finance()
finance.create_table()


class FSMAdmin(StatesGroup):
    name = State()
    last_name = State()


async def user_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply("Enter password")


async def name_enter(message: types.Message, state: FSMContext):
    if message.text == '1234':
        async with state.proxy() as data:
            data["name"] = message.text
        user = finance.get_user_id()
        await message.reply(f"You can see users_id {user}")
        await state.finish()
    else:
        await message.answer("Fuck you")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["User"], state=None)
    dp.register_message_handler(name_enter,  state=FSMAdmin.name)
