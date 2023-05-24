from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import executor
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.builtin import CommandHelp

openai.api_key = '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'
bot = Bot(token='6116196699:AAFuaTa_k3OrOwBnhu3vLwEOSrLDg1l_7Gw')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)