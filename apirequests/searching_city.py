import json
import re
import requests
from loguru import logger
from telebot import types
from loader import bot
from config_data.config import RAPID_API_KEY
from models.exceptions import TimeOut


def search_city(city: str, message: types.Message) -> dict:
    """
    Функция поиска id города через api
    :param city: str
    :return: dict
    """
    url = "https://hotels4.p.rapidapi.com/locations/search"

    querystring = {"query": city, "locale": "ru_RU"}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_KEY
    }
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        parsing = json.loads(response.text)
    except TimeOut as error:
        logger.error(f'error: {error}')
        bot.send_message(message.from_user.id, text='Превышено время ожидания, попробуйте позже')
        raise TimeOut("TimeOut")
    cities = dict()
    for suggestion in parsing['suggestions']:
        for entity in suggestion['entities']:
            if entity['type'] == 'CITY':
                caption = entity.get('caption', 'no information')
                text_filter = re.sub(r'<(.*?)>', '', caption)
                cities[text_filter] = entity.get('destinationId', False)
    return cities
