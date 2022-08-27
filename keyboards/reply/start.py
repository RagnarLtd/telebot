from telebot import types

def keyboard_start():
    keyboard_start = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    key_lowprice = types.KeyboardButton(text='/lowprice')
    key_highprice = types.KeyboardButton(text='/highprice')
    key_bestdeal = types.KeyboardButton(text='/bestdeal')
    key_help = types.KeyboardButton(text='/help')
    key_history = types.KeyboardButton(text='/history')
    keyboard_start.add(key_lowprice, key_bestdeal, key_highprice, key_help, key_history)
    return keyboard_start