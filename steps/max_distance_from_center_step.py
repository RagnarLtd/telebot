import re
from telebot import types
from keyboards.inline.yes_no import keyboard_yes_no
from models.user import User
from loader import bot


def max_distance_from_center(message: types.Message) -> None:
    """
    Функция обработки расстояния от центра города от юзера
    запрос необходимости фотографий
    """
    user = User.get_user(message.chat.id)
    pattern = re.search(r'[1-9]+[0-9]{0,}', message.text)
    if pattern:
        user.distance_max = int(pattern.group())
        bot.send_message(chat_id=message.chat.id,
                         text='Нужны ли фотографии отеля',
                         reply_markup=keyboard_yes_no())
        # bot.register_next_step_handler(message, photo_quantity)
    else:
        bot.send_message(chat_id=message.chat.id,
                         text='*Число введено не верно, попробуйте еще раз*',
                         parse_mode='Markdown')
        bot.register_next_step_handler(message, max_distance_from_center)
