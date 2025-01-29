class User:
    def __init__(self, user_id, name, email, password, role_id):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password  # Passwort sollte später gehasht werden
        self.role_id = role_id

    def check_password(self, password):
        """Einfache Passwortprüfung (später mit Hashing verbessern)"""
        return self.password == password