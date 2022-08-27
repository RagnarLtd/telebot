from database.Connection_to_DB import db
from models.default_models import History


def initialization_bd() -> None:
    with db:
        db.create_tables([History])


def writeHistory(database: db,
                 user_id: int,
                 days: int,
                 command: str,
                 hotels: dict) -> None:
    """
    Функция записи истории в базуданных
    :param database: db
    :param user_id: int
    :param days: int
    :param command: str
    :param hotels: dict
    :return: None
    """
    with db:
        database.create(user_id=user_id, req_days=days, user_command=command, hotels_found=hotels)


def get_info_from_db(database: db, user_id: int) -> list:
    """
    Функция получения информации из базыданных для вывода истории
    :param database: History
    :param user_id: int
    :return:
    """
    temporary = database.select().where(database.user_id == user_id).order_by(database.id.desc()).limit(3)
    data = list()
    for element in temporary:
        data.append([element.user_command, element.req_days, eval(element.hotels_found)])
    data.reverse()
    return data


def delete_info_from_db(database: db, user_id: int) -> None:
    """
    Функция удаления истории
    :param database: db
    :param user_id: int
    :return: None
    """
    temporary = database.select().where(database.user_id == user_id).order_by(database.id.desc()).limit(5)
    slice_id = 0
    for element in temporary:
        slice_id = element.id
    database.delete().where(database.id < slice_id, database.user_id == user_id).execute()
