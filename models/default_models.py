import database
from peewee import Model, PrimaryKeyField, IntegerField, CharField, TextField


class History(Model):
    """
    Класс инстория для базыданных
    """
    id = PrimaryKeyField(unique=True)
    user_id = IntegerField()
    user_command = CharField()
    req_days = IntegerField()
    hotels_found = TextField()


    class Meta:
        db_table = 'history'
        database = database.Connection_to_DB.db
        order_by = id

