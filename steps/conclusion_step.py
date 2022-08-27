from telebot import types
from apirequests.searching_photos import search_photos
from keyboards.reply.start import keyboard_start
from models.user import User
from loader import bot
from steps.send_result_step import send_result


def conclusion(message: types.Message) -> None:
    """
    Функция вывода найденых отелей юзеру
    """
    user = User.get_user(message.from_user.id)
    temp_days = (user.check_out - user.check_in).days
    if user.photo_quantity != 'no':
        for key, value in user.hotels_dict.items():
            photos = [types.InputMediaPhoto(elem) for elem in search_photos(key, message)[:int(user.photo_quantity)]]
            bot.send_message(message.from_user.id,
                             text=send_result(value, temp_days),
                             disable_web_page_preview=True,
                             parse_mode='Markdown')
            bot.send_media_group(message.from_user.id, photos)
    else:
        for key, value in user.hotels_dict.items():
            bot.send_message(message.from_user.id,
                             text=send_result(value, temp_days),
                             disable_web_page_preview=True,
                             parse_mode='Markdown')
    bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())
