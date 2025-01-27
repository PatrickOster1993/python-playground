# userController.py
from model.user import User
from view.userView import UserView

# Verbindungsglied zwischen Model & View!
class UserController:
    def __init__(self):
        self.user = None # zu Beginn noch kein User vorhanden (*)
        self.view = None # (*)
    
    def createUser(self):
        # User erstellen und Daten in Konsole ausgeben!
    
    def updateUserEmail(self):
        # Email-Adresse aktualisieren!