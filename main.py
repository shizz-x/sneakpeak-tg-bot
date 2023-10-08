import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from dotenv import load_dotenv

from modls.UnpackFuncs import UnpackFuncs

# logger
logging.basicConfig(level=logging.INFO)

load_dotenv()

storage = MemoryStorage()
bot = Bot(os.environ.get('TG_TOKEN'))
dp = Dispatcher(bot=bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())

if __name__ == '__main__':
    from aiogram import executor

    UnpackFuncs(bot=bot, dp=dp)
    executor.start_polling(dp)
