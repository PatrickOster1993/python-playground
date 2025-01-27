# main.py
from controller.userController import UserController

if __name__ == "__main__":
    controller = UserController()
    
    # Benutzer erstellen
    controller.createUser()
    
    # Benutzer-E-Mail aktualisieren
    controller.updateUserEmail()