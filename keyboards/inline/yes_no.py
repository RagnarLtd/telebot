from telebot import types


def keyboard_yes_no():
    keyboard_yes_no = types.InlineKeyboardMarkup(row_width=2)
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    key_cancel = types.InlineKeyboardButton(text='cancel', callback_data='cancel')
    keyboard_yes_no.add(key_yes, key_no, key_cancel)
    return keyboard_yes_no