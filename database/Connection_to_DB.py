from config_data.config import MYPASSWORD
from peewee import MySQLDatabase

db = MySQLDatabase('TestDB', user='root', password=MYPASSWORD, host='localhost')
