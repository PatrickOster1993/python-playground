# userView.py
# für Nutzerein- und ausgaben!
class UserView:
    def displayUserInfo(self, userInfo):
        print(userInfo)
    
    def getUserInput(self):
        name = input("Bitte geben Sie Ihren Namen ein.")
        email = self.getUserEmail()
        return {"name": name, "email": email}
    
    def getUserEmail(self):
        email = input("Bitte gib eine Email-Adresse ein.")
        return email