import datetime
from telebot import types
from models.user import User
from telegram_bot_calendar import DetailedTelegramCalendar
from loader import bot


def check_out(message: types.Message) -> None:
    """
    Функция вызова календаря для выбора даты выезда
    """
    user = User.get_user(message.chat.id)
    check_out_date = datetime.date.fromisoformat(str(user.check_in)) + datetime.timedelta(days=1)
    calendar, step = DetailedTelegramCalendar(calendar_id=2,
                                              locale='ru',
                                              min_date=check_out_date).build()
    bot.send_message(message.chat.id, "Выберите дату выезда",
                     reply_markup=calendar)
