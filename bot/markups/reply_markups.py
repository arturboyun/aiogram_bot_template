from aiogram.types import ReplyKeyboardMarkup


def test():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Test')
    return markup
