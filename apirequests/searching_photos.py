import requests
from config_data.config import RAPID_API_KEY
from models.exceptions import TimeOut
from telebot import types
from loader import bot
from loguru import logger


def search_photos(id_hotel: int, message: types.Message) -> list:
    """
    Функция поиска фотографий по id отеля
    :param id_hotel: int
    :return: list
    """
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

    querystring = {"id": id_hotel}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_KEY
    }
    try:
        response = requests.get(url, headers=headers, params=querystring).json()
    except TimeOut as error:
        logger.error(f'error: {error}')
        bot.send_message(message.from_user.id, text='Превышено время ожидания, попробуйте позже')
        raise TimeOut("TimeOut")
    photos = list()
    for element in response["hotelImages"]:
         photos.append(element.get("baseUrl").replace('{size}', 'b').replace('https', 'http'))
    photos = photos[:5]
    return photos
