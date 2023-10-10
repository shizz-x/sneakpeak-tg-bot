from aiogram.types import Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, MenuButton, KeyboardButton, CallbackQuery, \
    PreCheckoutQuery, LabeledPrice


class ReplyKeyboard:

    @property
    def start_mk(self) -> ReplyKeyboardMarkup:
        mk = ReplyKeyboardMarkup(resize_keyboard=True)

        mk.add(
            KeyboardButton('🔎 Проверить сайт'), 
            KeyboardButton('🧮 Расчитать стоимость'), 
            KeyboardButton('💳 Сделать заказ'))
        mk.add(
            KeyboardButton('➕ Дополнительная информация'), 
            KeyboardButton('🎁 Акции'))
        mk.add(
            KeyboardButton('🆓 Реферальная система'))

        return mk
    
    @staticmethod
    def inline_url_mk(url:str):
        return InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти', url=url))


