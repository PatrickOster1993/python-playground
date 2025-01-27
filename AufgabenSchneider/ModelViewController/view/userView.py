# userView.py
# für Nutzerein- und ausgaben!
from user import User

class UserView:
    def displayUserInfo(self, userInfo):
        self.userInfo = userInfo
        # Informationen über den User in Konsole ausgeben!
        print(userInfo)
       
    def getUserInput(self):
        # Nutzereingaben (hier über Konsole, da keine GUI) und vornehmen und zurückgeben!
        name = input("Enter name:")
        email = input("Enter Email:")
        return {"Name:": name, "Email": email}
    def getUserEmail(self):
        # Nutzer gibt neue Email-Adresse ein - Wert wird zurückgegeben!
        new_email = input("Please enter new Email Adress")
        return new_email