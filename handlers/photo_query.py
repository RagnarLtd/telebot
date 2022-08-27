from handlers.photo_quantity_query import find_hotels
from keyboards.inline.photo import keyboard_photo
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
def photo_quantity(message) -> None:
    """
    Функция запроса количества фотографий у юзера
    """
    if message.data == 'no':
        find_hotels(message)
    else:
        bot.edit_message_reply_markup(message.from_user.id, message.message.id, reply_markup=None)
        bot.send_message(chat_id=message.from_user.id,
                         text='Ввыберите количество фотографий отеля',
                         reply_markup=keyboard_photo())
