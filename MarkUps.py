from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, MenuButton, KeyboardButton, CallbackQuery, \
    PreCheckoutQuery, LabeledPrice


class ReplyKeyboard:
  @staticmethod
  def gen_keyboard(*args:tuple[str]):
    for tup in args:
      for sec in tup:
        print(sec)


ad  =  [('123123', 'sssss'), (1213, 123)]
ReplyKeyboard.gen_keyboard(*ad)