from User import User
import os

user_db = User()

# neuen user erstellen
user_db.create(email="ali@ali.com", password="123456", name="ali")


# checken ob db erstellt wurde
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "db.db")
if os.path.exists(db_path):
    print("Database created successfully.")
else:
    print("Failed to create the database.")