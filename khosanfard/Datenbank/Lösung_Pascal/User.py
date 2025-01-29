import sqlite3
import os

class User:
    def __init__(self, db_name: str = "db.db"):
        self.__db_name = db_name
        
        # Initialize the database
        self.__initialize_db()
    
    def __initialize_db(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(script_dir, self.__db_name)
            
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    name TEXT NOT NULL
                )
            ''')
            connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
    
    def create(self, email: str, password: str, name: str):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(script_dir, self.__db_name)
            
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (email, password, name) VALUES (?, ?, ?)", (email, password, name))
            connection.commit()
            print(f"User {name} created successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
            