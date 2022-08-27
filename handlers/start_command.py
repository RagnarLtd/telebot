from telebot import types
from keyboards.reply.start import keyboard_start
from loader import bot


@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
    """
    Функция приветствия игрока
    """
    bot.send_message(message.from_user.id, 'Привет, {name}. Я - TooEasyTravelBot.'
                                           '\n Я помогу вам найти выгодное предложение по отелям'
                                           '\nна сайте Hotels.com. Выберите необходиммую команды.'
                                           '\nДля информации надмите /help' .format(name=message.from_user.first_name))
    bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())
