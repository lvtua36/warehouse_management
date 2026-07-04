import pymysql

from config import Config

class Database:

    @staticmethod
    def get_connection():

        return pymysql.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            db=Config.MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )