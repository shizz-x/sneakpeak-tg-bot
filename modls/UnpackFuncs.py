from aiogram import Dispatcher, types, Bot
from modls.MarkUps import ReplyKeyboard as KB
from modls.Utils import Utility
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
                        self.utils.add_user(msg.from_user.id)
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
            '➕': lambda x: self.__additional_info(x),
            '🎁': lambda x: self.__special_offers(x),
            '🆓': lambda x: self.__refferal_system(x),
        }

    async def __check_website(self, msg: types.Message) -> None:
        
            
        await msg.answer('Отправьте ссылку на сайт с которого хотите заказать товар: ')
        await __FSM__.message.set()


        @self.dp.message_handler(state=__FSM__.message)
        async def procces_answer(msg: types.Message, state: FSMContext):



            url_valid = self.utils.check_uri_exists(uri=msg.text)

            if url_valid:

                await msg.reply('Отсюда можно заказать')
            else:
                await msg.reply('Пока что не можем привезти, но вы можете обратиться в поддержку для предложения рассмотрения этого сайта.')
            await state.finish()

        return None
    async def __gen_price(self, msg: types.Message) -> None:
        await msg.answer('Отправьте цену в долларах для расчета стоимость товара с учетом доставки:')
        await __FSM__.message.set()


        @self.dp.message_handler(state=__FSM__.message)
        async def procces_answer(msg: types.Message, state: FSMContext):
            try:
                await msg.reply(str(int(msg.text) * 107 + 6000) + ' цена в рублях')
            except Exception as e:
                await msg.reply('Введите корректную целую сумму')
            finally:
                await state.finish()


        pass
    async def __make_deal(self, msg: types.Message) -> None:
        await msg.answer('Удачных покупок :)', reply_markup=self.keyboard.inline_url_mk('https://t.me/sneakerivan'))

        
    async def __special_offers(self, msg: types.Message) -> None:
        await msg.answer('Какие то акции', reply_markup=self.keyboard.inline_url_mk('https://t.me/sneakpeakusa/3'))


    async def __additional_info(self, msg: types.Message) -> None:
        await msg.answer('Обязательно к прочтению', reply_markup=self.keyboard.inline_url_mk('https://t.me/sneakpeakusa/3'))


    async def __refferal_system(self, msg: types.Message) -> None:
        
        await self.bot.send_message(msg.from_user.id, f"Ваша реферальная ссылка <a href='https://t.me/Sneakers_Peak_Bot?start={msg.from_user.id}'>URL</a>\nКоличество ваших рефералов: {self.utils.get_referrals(msg.from_user.id)}\nБаланс: {self.utils.get_balance(msg.from_user.id)}руб", parse_mode='HTML')



