from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, MenuButton, KeyboardButton, CallbackQuery, \
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
            KeyboardButton('ℹ️ Дополнительная информация'), 
            KeyboardButton('🎁 Акции'))
        mk.add(
            KeyboardButton('🆓 Реферальная система'))

        return mk


