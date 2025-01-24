# user.py
# Hinweis: enthält lediglich Daten - weder Konsolenein- noch ausgabe (= strikte Trennung der Verantwortungsbereiche einzelner Klassen)!
class User:
    # Repräsentiert einen Benutzer mit Namen und E-Mail.
    def __init__(self, name, email):
        # Legt die Felder für Name und E-Mail fest.
        self.name = name
        self.email = email
    
    def updateEmail(self, newEmail):
        # Setzt eine neue E-Mail, sofern sie gültig ist, sonst Fehler.
        if "@" not in newEmail:
            raise ValueError("Ungültige E-Mail-Adresse")
        self.email = newEmail
    
    def getUserInfo(self):
        # Gibt eine kompakte Zeichenkette mit den Benutzerdaten zurück.
        return f"Name: {self.name}, E-Mail: {self.email}"