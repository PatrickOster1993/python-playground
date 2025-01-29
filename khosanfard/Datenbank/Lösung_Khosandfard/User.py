import sqlite3
class User:
    id: int
    email: str
    password: str
    name: str
    __db_name: str
    def __init__(self):
        self.__db_name = "db.db"
        connction = sqlite3.connect(self.__db_name)
        cursor = connction.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    name TEXT NOT NULL
                    )
                 ''')
        connction.commit()

        
    def create(self, email:str , password: str ,name:str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (email,name,password) VALUES (?,?,?)" , (email , name ,password))
        connection.commit()
    
    def list(self):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    
    def getSingleByEmail(self,email:str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()