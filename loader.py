from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
import logging

storage = MemoryStorage()

bot = Bot(token=TOKEN)

logging.basicConfig(level=logging.INFO)


dp = Dispatcher(bot, storage=storage)
