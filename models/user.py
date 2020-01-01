import sqlite3
from sqlite3 import Error
from core import Database
import os 

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db = Database()
        _PATH = os.path.join(os.path.abspath('.'), 'data.db')
        self.db.create_connection(r"{}".format(_PATH))

    def isUsernameUnique(self):
        sql = ''' SELECT * FROM users WHERE username="{}" '''.format(self.username)
        rows = self.db.select_record(sql)
        if len(rows) > 0:
            return False
        else:
            return True

    def registration(self):
        sql = '''INSERT INTO users(username,password) VALUES(?,?)'''
        print(self.db.insert_record(sql, (self.username, self.password)))
        

    def authenticate(self):
        sql = ''' SELECT * FROM users WHERE username="{}" AND password="{}" '''.format(self.username,self.password)

        rows = self.db.select_record(sql)

        return rows
        


    