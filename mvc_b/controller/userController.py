# userController.py
from model.user import User
from view.userView import UserView

# Verbindungsglied zwischen Model & View!
class UserController:
    def __init__(self):
        self.user = None # zu Beginn noch kein User vorhanden (*)
        self.view = None # (*)
    
    def createUser(self):
        self.view = UserView()
        input = self.view.getUserInput()
        self.user = User(input["name"], input["email"])

    def updateUserEmail(self):
        self.user.updateEmail(self.view.getUserEmail())
        self.view.displayUserInfo(self.user.getUserInfo())
