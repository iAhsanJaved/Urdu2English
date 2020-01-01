import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            self.conn = sqlite3.connect(db_file)
            return self.conn
        except Error as e:
            print(e)
    
        return self.conn
    
    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_record(self, sql, data):
        """
        Create a record
        :param sql:
        :param data:
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute(sql, data)
            self.conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)
        return None
    
    def update_record(self, sql, data):
        """
        Update a record
        :param sql:
        :param data:
        :return:
        """
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def select_record(self, sql):
        """
        Select record
        :param sql:
        :return:
        """
        cur = self.conn.cursor()
        cur.execute(sql)
    
        rows = cur.fetchall()
    
        return rows
    
    def delete_record(self, sql):
        """
        Delete record
        :param sql:
        :return:
        """
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()