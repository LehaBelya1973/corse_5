from config import config
from db_manager import DBManager

params = config()
db = DBManager(db_name='db_name', **params)
