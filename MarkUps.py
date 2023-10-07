from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, MenuButton, KeyboardButton, CallbackQuery, \
    PreCheckoutQuery, LabeledPrice


class ReplyKeyboard:

    @property
    def start_mk(self) -> ReplyKeyboardMarkup:
        mk = ReplyKeyboardMarkup(resize_keyboard=True)

        mk.add(KeyboardButton('aweaw'), KeyboardButton('aweaw'))

        return mk


