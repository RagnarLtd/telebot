from telebot import types


def keyboard_cancel():
    keyboard_cancel = types.InlineKeyboardMarkup()
    key_cancel = types.InlineKeyboardButton(text='cancel', callback_data='cancel')
    keyboard_cancel.add(key_cancel)
    return keyboard_cancel