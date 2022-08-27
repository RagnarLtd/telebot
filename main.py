from loguru import logger
from database.functionswithBD import initialization_bd
from loader import bot
import handlers


if __name__ == "__main__":
    initialization_bd()
    logger.add('logs.log', rotation='100 MB')
    bot.infinity_polling()
