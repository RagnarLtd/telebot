from telebot import types
from keyboards.reply.start import keyboard_start
from loader import bot


@bot.message_handler(commands=['help'])
def help_command(message: types.Message) -> None:
    """
    Функция вызова информации по команде /help
    """
    text = 'Основные команды:'\
           '\nhelp - помощь по командам бота.'\
           '\nlowprice - вывод самых дешевых отелей в городе.'\
           '\nhighprice - вывод самых дорогих отелей в городе.'\
           '\nbestdeal - вывод отелей, наиболее подходящих по цене'\
           ' и расположению от центра'\
           '\nhistory - вывод истории поиска отелей'
    bot.send_message(message.chat.id, text=text)
    bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())