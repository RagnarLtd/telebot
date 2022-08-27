import datetime
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar
from loader import bot


def check_in(message: types.Message) -> None:
    """
    Функция вызова календаря для выбора даты заезда
    """
    date = datetime.date.today()
    calendar, step = DetailedTelegramCalendar(calendar_id=1,
                                              locale='ru',
                                              min_date=date).build()
    bot.send_message(message.chat.id, "Выберите дату заезда", reply_markup=calendar)
