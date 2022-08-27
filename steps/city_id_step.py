from loguru import logger
from telebot import types
from keyboards.reply.start import keyboard_start
from models.user import User
from loader import bot
from steps.check_in_step import check_in


def city_id(message: types.Message) -> None:
    """
    Функция получения id города, после уточнения юзера
    """
    user = User.get_user(message.chat.id)
    if message.text == 'Отмена':
        bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())
    else:
        try:
            user = User.get_user(message.chat.id)
            user.city_id = user.city_id_list[message.text]
            check_in(message)
        except Exception as error:
            logger.error(f'error: {error}')
            bot.send_message(message.chat.id,
                             text='*У выбранного города нет id, попробуйте сначала*',
                             parse_mode="Markdown")
            bot.send_message(message.from_user.id,
                             text='Выберите команду',
                             reply_markup=keyboard_start())
