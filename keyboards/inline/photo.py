from telebot import types


def keyboard_photo():
    keyboard_photo = types.InlineKeyboardMarkup(row_width=5)
    key_1 = types.InlineKeyboardButton(text='1', callback_data='1')
    key_2 = types.InlineKeyboardButton(text='2', callback_data='2')
    key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
    key_4 = types.InlineKeyboardButton(text='4', callback_data='4')
    key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
    key_cancel = types.InlineKeyboardButton(text='cancel', callback_data='cancel')
    keyboard_photo.add(key_1, key_2, key_3, key_4, key_5, key_cancel)
    return keyboard_photo