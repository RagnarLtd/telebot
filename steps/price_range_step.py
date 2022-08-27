import re
from telebot import types
from keyboards.inline.cancel import keyboard_cancel
from models.user import User
from loader import bot
from steps.max_distance_from_center_step import max_distance_from_center


def price_range(message: types.Message) -> None:
    """
    Функция обработки минимальной и максимальной цены
    за одну ночь от юзера
    запрос расстояния от центра
    """
    user = User.get_user(message.chat.id)
    pattern = re.search(r'[1-9]+[0-9]{1,} [1-9]+[0-9]{1,}', message.text)
    if pattern:
        minimum, maximum = pattern.group().split()
        if minimum > maximum:
            minimum, maximum = maximum, minimum
        user.price_min = minimum
        user.price_max = maximum
        bot.send_message(chat_id=message.chat.id,
                         text='Введите расстояние максимальное расстояние от центра в метрах',
                         reply_markup=keyboard_cancel())
        bot.register_next_step_handler(message, max_distance_from_center)
    else:
        bot.send_message(message.chat.id, text='*Диапазон введен не верно, повторите ввод*', parse_mode='Markdown')
        bot.register_next_step_handler(message, price_range)