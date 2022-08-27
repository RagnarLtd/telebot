from telebot import types
from keyboards.inline.yes_no import keyboard_yes_no
from models.user import User
from loader import bot
from steps.price_range_step import price_range


def hotels_quantity(message: types.Message) -> None:
    """
    Функция обработки количесва отелей от ответа юзера
    запрос минимальной и максимальной цены за ночь
    """
    if message.text.isdigit():
        if 1 <= int(message.text) <= 5:
            user = User.get_user(message.chat.id)
            user.hotels_quantity = message.text
            if user.command == '/bestdeal':
                bot.send_message(message.chat.id,
                                 text='Введите минимальную и максимальную цену за 1 ночь(через пробел)')
                bot.register_next_step_handler(message, price_range)
            else:
                bot.send_message(message.chat.id,
                                 text='Нужны ли фотографии отеля',
                                 reply_markup=keyboard_yes_no())
        else:
            bot.send_message(message.chat.id,
                             text='Вы ввели некорректное число. Введите еще раз, оно не должно превышать 5')
            bot.register_next_step_handler(message, hotels_quantity)
    else:
        bot.send_message(message.chat.id, text='Вы ввели не число. Попробуйте еще раз')
        bot.register_next_step_handler(message, hotels_quantity)