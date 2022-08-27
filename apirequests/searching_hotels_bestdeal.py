import requests
import time
from config_data.config import RAPID_API_KEY
from loguru import logger
from models.exceptions import TimeOut
from loader import bot

def search_hotels_bestdeal(id_of_city: int, checkin: str, checkout: str,
                           price_min: str, price_max: str, distance_max: int, user_id: str) -> dict:
    """
    Функция поиска отелей по выбарнным параментрам юзера для bestdeal
    :param id_of_city: int
    :param checkin: str
    :param checkout: str
    :param price_min: str
    :param price_max: str
    :param distance_max: int
    :param user_id: str
    :return: dict
    """
    count = 1
    hotels_best = dict()
    while True:
        url = "https://hotels4.p.rapidapi.com/properties/list"

        querystring = {"destinationId": id_of_city,
                       "pageNumber": count,
                       "pageSize": "25",
                       "checkIn": checkin,
                       "checkOut": checkout,
                       "adults1": "1",
                       "priceMin": price_min,
                       "priceMax": price_max,
                       "sortOrder": 'DISTANCE_FROM_LANDMARK',
                       "locale": "ru_RU",
                       "currency": "RUB"}
        headers = {
            'x-rapidapi-host': "hotels4.p.rapidapi.com",
            'x-rapidapi-key': RAPID_API_KEY
        }
        try:
            response = requests.get(url, headers=headers, params=querystring, timeout=40).json()
        except TimeOut as error:
            logger.error(f'error: {error}')
            bot.send_message(user_id, text='Превышено время ожидания, попробуйте позже')
            raise TimeOut("TimeOut")
        for result in response['data']['body']['searchResults']['results']:
            try:
                idhotel = result.get('id')
                name = result.get('name')
                address = result['address'].get('streetAddress')
                if not address: address = result['address'].get('locality')
                price = result.get('ratePlan', False).get('price').get('current').split()[0].replace(',', '')
                distance = result['landmarks'][0]['distance']
                from_center = round((float(distance.split()[0].replace(',', '.')) * 1609), 2)
                if from_center <= distance_max:
                    from_center = round((from_center / 1000), 2)
                    if from_center == 0: from_center = 'В центре города'
                    urlhotel = 'https://ru.hotels.com/ho{id}'.format(id=idhotel)
                    hotels_best[idhotel] = price, name, address, str(from_center), urlhotel
            except Exception as error:
                logger.error(f'error: {error}')
        pagination = response['data']['body']['searchResults'].get('pagination', False)
        if pagination:
            next_page = pagination.get('nextPageNumber', False)
        else:
            break
        if 0 < next_page <= 2:
            count = int(next_page)
        else:
            break
        time.sleep(0.5)
    hotels = {keys: values for keys, values in sorted(hotels_best.items(),
                                                      key=lambda item: item[1],
                                                      reverse=True)}
    return hotels
