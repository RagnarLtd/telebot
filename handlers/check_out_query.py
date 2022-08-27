import datetime
from telebot import types
from models.user import User
from telegram_bot_calendar import DetailedTelegramCalendar
from loader import bot
from keyboards.inline.cancel import keyboard_cancel
from steps.hotels_quantity_step import hotels_quantity


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def cal(callback_query: types.CallbackQuery):
    user = User.get_user(callback_query.from_user.id)
    check_out_date = datetime.date.fromisoformat(str(user.check_in)) + datetime.timedelta(days=1)
    result, key, step = DetailedTelegramCalendar(calendar_id=2,
                                                 locale='ru',
                                                 min_date=check_out_date).process(callback_query.data)
    if not result and key:
        bot.edit_message_text("Выберите дату выезда",
                              callback_query.message.chat.id,
                              callback_query.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"Вы выбрали {result}",
                              callback_query.message.chat.id,
                              callback_query.message.message_id)
        user.check_out = result
        message = bot.send_message(chat_id=callback_query.message.chat.id,
                                   text='Введите количество отелей, но не более 5',
                                   reply_markup=keyboard_cancel())
        bot.register_next_step_handler(message, hotels_quantity)