# main.py
from userController import UserController

if __name__ == "__main__":
    # Erstellt einen UserController und führt exemplarische Methoden zur Demonstration aus.
    controller = UserController()
    
    # Benutzer erstellen
    controller.createUser()
    
    # Benutzer-E-Mail aktualisieren
    controller.updateUserEmail()