class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state} {self.zip}'