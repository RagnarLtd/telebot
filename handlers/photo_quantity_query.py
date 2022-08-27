import itertools
from loguru import logger
from apirequests.searching_hotels import search_hotels
from apirequests.searching_hotels_bestdeal import search_hotels_bestdeal
from database.functionswithBD import  writeHistory, delete_info_from_db
from keyboards.reply.start import keyboard_start
from models import default_models
from models.user import User
from loader import bot
from steps.conclusion_step import conclusion


@bot.callback_query_handler(func=lambda call: '1' <= call.data <= '5')
def find_hotels(message) -> None:
    """
    Функция запроса списка отелей от api
    """
    user = User.get_user(message.from_user.id)
    user.photo_quantity = message.data
    hotels = {}
    bot.edit_message_reply_markup(message.from_user.id, message.message.id, reply_markup=None)
    msg = bot.send_message(message.from_user.id, text='Подождите, идёт поиск отелей...')
    if user.command == '/lowprice':
        try:
            hotels = search_hotels(user.city_id,
                                   user.check_in,
                                   user.check_out,
                                   'PRICE',
                                   message.from_user.id,
                                   user.hotels_quantity
                                   )
        except Exception as error:
            logger.error(f'error: {error}')
            bot.send_message(message.from_user.id, text='Наблюдаются проблемы с api, попробуйте позже')
    elif user.command == '/highprice':
        try:
            hotels = search_hotels(user.city_id,
                                   user.check_in,
                                   user.check_out,
                                   'PRICE_HIGHEST_FIRST',
                                   message.from_user.id,
                                   user.hotels_quantity
                                   )
        except Exception as error:
            logger.error(f'error: {error}')
            bot.send_message(message.from_user.id, text='Наблюдаются проблемы с api, попробуйте позже')
    elif user.command == '/bestdeal':
        try:
            hotels = search_hotels_bestdeal(user.city_id,
                                            user.check_in,
                                            user.check_out,
                                            user.price_min,
                                            user.price_max,
                                            user.distance_max,
                                            message.from_user.id
                                            )
        except Exception as error:
            logger.error(f'error: {error}')
            bot.send_message(message.from_user.id, text='Наблюдаются проблемы с api, попробуйте позже')
        hotels = dict(itertools.islice(hotels.items(), int(user.hotels_quantity)))

    if len(hotels) != 0:
        bot.delete_message(chat_id=message.from_user.id, message_id=msg.message_id)
        user.hotels_dict = hotels
        required_days = (user.check_out - user.check_in).days
        writeHistory(default_models.History, user.user_id, required_days, user.command, user.hotels_dict)
        delete_info_from_db(default_models.History, user.user_id)
        conclusion(message)
    else:
        bot.delete_message(chat_id=message.from_user.id, message_id=msg.message_id)
        bot.send_message(message.from_user.id, text='По вашему запросу ничего не найдено')
        bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())