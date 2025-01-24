# userView.py
# für Nutzerein- und ausgaben!
# Die Klasse UserView verwaltet Interaktionen mit Nutzern, z.B. Ein- und Ausgaben.
class UserView:
    # Diese Klasse dient der Darstellung und Eingabe von Benutzerinformationen.
    def displayUserInfo(self, userInfo):
        # Gibt die erhaltenen Benutzerdaten formatiert auf der Konsole aus.
        print("\n=== Benutzerinformation ===")
        print(userInfo)
    
    def getUserInput(self):
        # Fragt den Benutzer nach einem Namen und prüft, ob dieser nicht leer ist.
        # Fordert den Nutzer zur Eingabe eines Namens auf und prüft auf Leerzeile.
        name = input("Bitte Namen eingeben: ").strip()
        while not name:
            # Wiederholtes Abfragen, bis ein gültiger Name eingegeben wurde.
            name = input("Name darf nicht leer sein! Bitte erneut eingeben: ").strip()
        return name
    
    def getUserEmail(self):
        # Fragt den Benutzer nach einer E-Mail und überprüft das Format.
        # Fordert den Nutzer zur Eingabe einer E-Mail-Adresse auf und prüft das Format.
        email = input("Bitte E-Mail-Adresse eingeben: ").strip()
        while "@" not in email:
            # Wiederholtes Abfragen, bis eine gültige E-Mail-Adresse eingegeben wurde.
            email = input("Ungültiges Format! Bitte gültige E-Mail eingeben: ").strip()
        return email