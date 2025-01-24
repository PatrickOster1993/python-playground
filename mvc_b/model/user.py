# Hinweis: enthält lediglich Daten - weder Konsolenein- noch ausgabe (= strikte Trennung der Verantwortungsbereiche einzelner Klassen)!
class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    def updateEmail(self, newEmail):
        self.__email = newEmail
    
    def getUserInfo(self):
        return {"name" : self.__name, "email" : self.__email}