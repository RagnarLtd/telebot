class User:
    users = {}
    """
    Класс описывающий пользователя
    """
    def __init__(self, user_id: int, loc_lang: str = 'ru_RU') -> None:
        self.user_id = user_id
        self.loc_lang = loc_lang
        self.name_city = None
        self.command = None
        self.city_id = None
        self.city_id_list = None
        self.hotels_quantity = None
        self.hotels_dict = None
        self.photo_quantity = None
        self.photo_id_list = None
        self.price_min = None
        self.price_max = None
        self.distance_min = None
        self.distance_max = None
        self.check_in = None
        self.check_out = None


    @staticmethod
    def get_user(user_id):
        if User.users.get(user_id) is None:
            new_user = User(user_id)
            return new_user
        return User.users.get(user_id)

    @classmethod
    def add_user(cls, user_id, user):
        cls.users[user_id] = user
