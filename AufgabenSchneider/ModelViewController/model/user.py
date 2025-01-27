# user.py
# Hinweis: enthält lediglich Daten - weder Konsolenein- noch ausgabe (= strikte Trennung der Verantwortungsbereiche einzelner Klassen)!
class User:
    def __init__(self, name, email):
        # Attribute zuweisen
        self.__name = name
        self.__email = email
    
    def updateEmail(self, newEmail):
        # Email-Adresse ändern
        self.__newEmail = newEmail
    
    def getUserInfo(self):
        # Infos zu User zurückgeben
        return{"Name:": self.__name, "Email": self.__newEmail}