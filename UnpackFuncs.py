from aiogram import Dispatcher, types


class UnpackFuncs:
    dp: Dispatcher

    def __init__(self, dp: Dispatcher):
        @dp.message_handler(commands=['start', 'help'])
        async def send_welcome(message: types.Message):
            await message.reply("Hi!\nI'm EchoBot!")
