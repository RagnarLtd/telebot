from telebot import types
from database.functionswithBD import get_info_from_db
from keyboards.reply.start import keyboard_start
from models import default_models
from loader import bot


@bot.message_handler(commands=['history'])
def history_command(message: types.Message) -> None:
    """
    Функция вызова истории по user_id
    """
    data = get_info_from_db(default_models.History, message.chat.id)
    if len(data) != 0:
        for element in data:
            command = element[0].replace('/', '')
            bot.send_message(message.chat.id, text=f'*Выбранная команда*: _{command}_', parse_mode="Markdown")
            for key, value in element[2].items():
                bot.send_message(message.chat.id,
                                 text=f'*Наименование отеля*: [{value[1]}]({value[4]})'
                                      f'\n*Адрес отеля*: _{value[2]}_'
                                      f'\n*Стоимость за ночь*: _{value[0]}_ руб.'
                                      f'\n*Стоимость за выбранный период*: _{int(value[0]) * int(element[1])}_ руб.'
                                      f'\n*Расстояние от центра города*: _{value[3]}_ км',
                                 disable_web_page_preview=True,
                                 parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, text='История пока пуста')
    bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())
