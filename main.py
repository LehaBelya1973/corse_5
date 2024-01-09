from src.config import config
from src.db_manager import DBManager

params = config()
db = DBManager(db_name='db_name', **params)
