import sqlite3
from sqlite3 import Error
from core import Database
import os 
from datetime import datetime

class Translate:
    def __init__(self, translated_result, user_id):
        self.translated_result = translated_result
        self.user_id = user_id
        self.db = Database()
        _PATH = os.path.join(os.path.abspath('.'), 'data.db')
        self.db.create_connection(r"{}".format(_PATH))

    def storeResult(self):
        sql = '''INSERT INTO translate(translated_result,user_id,created_on) VALUES(?,?,?)'''
        current_datetime = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        print(self.db.insert_record(sql, (self.translated_result, self.user_id, current_datetime)))
        




    