from telebot import types
from keyboards.inline.cancel import keyboard_cancel
from models.user import User
from loader import bot
from steps.cities_id_step import cities_id


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def take_up_command(message: types.Message) -> None:
    """
    Функция отлавливания основных поисковых комманд бота
    с последующим запросом города
    """
    user = User.get_user(message.chat.id)
    user.add_user(message.chat.id, user)
    user.command = message.text
    bot.send_message(message.chat.id, 'Введите город для поиска', reply_markup=keyboard_cancel())
    bot.register_next_step_handler(message, cities_id)
