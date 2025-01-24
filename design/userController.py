# userController.py
from user import User
from userView import UserView

# Verbindungsglied zwischen Model & View!
class UserController:
    # Verwaltet die Erstellung und Aktualisierung eines Benutzerobjekts.
    def __init__(self):
        # Initialisiert das User-Objekt und eine zugehörige View.
        self.user = None
        self.view = UserView()
    
    def createUser(self):
        # Erfragt Benutzerdaten über die View
        # und legt ein neues User-Objekt an, das anschließend angezeigt wird.
        name = self.view.getUserInput()
        email = self.view.getUserEmail()
        self.user = User(name, email)
        self.view.displayUserInfo(self.user.getUserInfo())
    
    def updateUserEmail(self):
        # Aktualisiert die E-Mail, wenn ein User vorhanden ist, sonst Fehlermeldung.
        if not self.user:
            print("Fehler: Es existiert kein Benutzer!")
            return
        new_email = self.view.getUserEmail()
        self.user.updateEmail(new_email)
        self.view.displayUserInfo("Erfolgreich aktualisiert:\n" + self.user.getUserInfo())