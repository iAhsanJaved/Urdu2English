from core import Database

# Step-1: Create database object
db = Database()
# Step-2: Create connection
db.create_connection('data.db')
# Step-3: Create Users table
sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """
db.create_table(sql_create_users_table)
# Step-4: Create Translate table
sql_create_translate_table = """ CREATE TABLE IF NOT EXISTS translate (
                                        id integer PRIMARY KEY,
                                        translated_result text NOT NULL,
                                        user_id integer NOT NULL,
                                        created_on text NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (id)
                                    ); """
db.create_table(sql_create_translate_table)

