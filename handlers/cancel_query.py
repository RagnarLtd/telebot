from keyboards.reply.start import keyboard_start
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data == 'cancel')
def cancel(message) -> None:
    """
    Функция отмены, если inlinebutton "cancel"
    """
    bot.clear_step_handler_by_chat_id(chat_id=message.from_user.id)
    bot.edit_message_reply_markup(message.from_user.id, message.message.id, reply_markup=None)
    bot.send_message(message.from_user.id, text='Выберите команду', reply_markup=keyboard_start())
