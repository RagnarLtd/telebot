import json
import requests
from config_data.config import RAPID_API_KEY
from loguru import logger
from models.exceptions import TimeOut
from loader import bot


def search_hotels(id_of_city: int,
                  checkin: str,
                  checkout: str,
                  sort: str,
                  user_id: str,
                  hotels_quantity: str = '5') -> dict:
    """
    Функция поиска отелей по выбарнным параментрам юзера для lowprice and highprice
    :param id_of_city: int
    :param checkin: str
    :param checkout: str
    :param sort: str
    :param user_id: str
    :param hotels_quantity: str
    :return: dict
    """
    url2 = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {"destinationId": id_of_city,
                   "pageNumber": "1",
                   "pageSize": hotels_quantity,
                   "checkIn": checkin,
                   "checkOut": checkout,
                   "adults1": "1",
                   "sortOrder": sort,
                   "locale": "ru_RU",
                   "currency": "RUB"}
    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_KEY
    }
    try:
        response = requests.get(url2, headers=headers, params=querystring, timeout=10)
        parsing1 = json.loads(response.text)
    except TimeOut as error:
        logger.error(f'error: {error}')
        bot.send_message(user_id, text='Превышено время ожидания, попробуйте позже')
        raise TimeOut("TimeOut")

    hotels = dict()
    for result in parsing1['data']['body']['searchResults']['results']:
        try:
            idhotel = result.get('id')
            name = result.get('name')
            address = result['address'].get('streetAddress')
            if not address: address = result['address'].get('locality')
            price = result.get('ratePlan')
            if not price:
                price = 0
            else:
                price = result['ratePlan']['price'].get('current', False).split()[0].replace(',', '')
            distance = result['landmarks'][0]['distance']
            from_center = round((float(distance.split()[0].replace(',', '.')) * 1.60934), 2)
            if from_center == 0: from_center = 'В центре города'
            urlhotel = 'https://ru.hotels.com/ho{id}'.format(id=idhotel)
            hotels[idhotel] = price,  name, address, str(from_center), urlhotel
        except Exception as error:
            logger.error(f'error: {error}')
    return hotels
