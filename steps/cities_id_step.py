import re
import requests
from loguru import logger
from telebot import types
from apirequests.searching_city import search_city
from keyboards.reply.cities import cities_keyboard
from keyboards.reply.start import keyboard_start
from models.exceptions import ZeroHotels
from models.user import User
from loader import bot
from steps.city_id_step import city_id


def cities_id(message: types.Message) -> None:
    """
    Функция для уточнения города из списка
    полученного от api
    """
    user = User.get_user(message.chat.id)
    text_mes = message.text
    pattern = re.findall(r'\b[a-zA-Zа-яА-ЯёЁ\s]+', text_mes)
    try:
        cities_all = search_city(pattern, message)
        if len(cities_all) == 0:
            raise ZeroHotels('Такого города не найдено')
        user.city_id_list = cities_all
        bot.send_message(message.chat.id,
                         text='Уточните город',
                         reply_markup=cities_keyboard(cities_all))
        bot.register_next_step_handler(message, city_id)
    except requests.exceptions.RequestException as error:
        logger.error(f'error: {error}')
        bot.send_message(message.chat.id, text='*Программа не отвечает, повторите запрос позже*', parse_mode="Markdown")
        bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())
    except Exception as error:
        logger.error(f'error: {error}')
        bot.send_message(message.chat.id, text='*Введен неверный запрос, попробуйте еще раз*', parse_mode="Markdown")
        bot.register_next_step_handler(message, cities_id)
