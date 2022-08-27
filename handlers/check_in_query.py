import datetime
from telebot import types
from models.user import User
from telegram_bot_calendar import DetailedTelegramCalendar
from loader import bot
from steps.chech_out_step import check_out


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def cal(callback_query: types.CallbackQuery):
    date = datetime.date.today()
    result, key, step = DetailedTelegramCalendar(calendar_id=1,
                                                 locale='ru',
                                                 min_date=date).process(callback_query.data)
    if not result and key:
        bot.edit_message_text("Выберите дату заезда",
                              callback_query.message.chat.id,
                              callback_query.message.message_id,
                              reply_markup=key)

    elif result:
        bot.edit_message_text(f"Вы выбрали {result}",
                              callback_query.message.chat.id,
                              callback_query.message.message_id)
        user = User.get_user(callback_query.from_user.id)
        user.check_in = result
        check_out(callback_query.message)