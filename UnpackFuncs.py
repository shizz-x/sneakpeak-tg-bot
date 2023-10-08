from aiogram import Dispatcher, types, Bot
from MarkUps import ReplyKeyboard as KB
from Utils import Utility
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext



class __FSM__(StatesGroup):
    message = State()



class UnpackFuncs:
    dp: Dispatcher
    keyboard: KB
    bot: Bot

    def __init__(self, bot: Bot, dp: Dispatcher):
        self.dp =       dp
        self.keyboard = KB()
        self.bot =      bot
        self.utils =    Utility()


        self.__unpack()

    def __unpack(self):

        @self.dp.message_handler(commands=['start'])
        async def start(msg: types.Message):

            start_command = msg.text
            referrer_id = start_command[7:]



            if referrer_id != '':
                if referrer_id != str(msg.from_user.id):
                    try:
                        self.utils.add_user(msg.from_user.id, int(referrer_id))
                        await self.bot.send_message(referrer_id, 'НОВЫЙ РЕФЧИК ПОДЪЕХАЛ')
                    except Exception as e:
                        print(e)
                        pass
                else:
                    self.utils.add_user(msg.from_user.id)
                    
            else:
                self.utils.add_user(msg.from_user.id)
            await msg.reply(
                'SEE YA', 
                reply_markup=self.keyboard.start_mk
            )

        
        @self.dp.message_handler(content_types=['text'])
        async def message_handler(msg: types.Message):
            
            first_letter = msg.text[0].lower()

            if first_letter in list(self.__funcs.keys()):
                
                await self.__funcs.get(first_letter)(msg)

    @property
    def __funcs(self) -> dict:

        return {
            '🔎': lambda x: self.__check_website(x),
            '🧮': lambda x: self.__gen_price(x),
            '💳': lambda x: self.__make_deal(x),
            'ℹ️': lambda x: self.__additional_info(x),
            '🎁': lambda x: self.__special_offers(x),
            '🆓': lambda x: self.__refferal_system(x),
        }

    async def __check_website(self, msg: types.Message) -> None:
        await msg.answer('send an uri')
        await __FSM__.message.set()


        @self.dp.message_handler(state=__FSM__.message)
        async def procces_answer(msg: types.Message, state: FSMContext):
            await msg.reply(msg.text)
            await state.finish()

        return None
    async def __gen_price(self) -> None:
        pass
    async def __make_deal(self) -> None:
        pass
    async def __special_offers(self) -> None:
        pass
    async def __additional_info(self) -> None:
        pass
    async def __refferal_system(self, msg: types.Message) -> None:
        
        await self.bot.send_message(msg.from_user.id, f"<a href='https://t.me/Sneakers_Peak_Bot?start={msg.from_user.id}'>URL</a>", parse_mode='HTML')
        pass



