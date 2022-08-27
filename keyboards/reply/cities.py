from telebot import types


def cities_keyboard(cities: dict):
    keyboard_cities = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True)
    for element in cities.keys():
        keyboard_cities.add(types.KeyboardButton(text=element))
    key_cancel = types.KeyboardButton(text='Отмена')
    keyboard_cities.add(key_cancel)
    return keyboard_cities