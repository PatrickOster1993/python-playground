class Customer:
    def __init__(self, name: str, address: str, customer_id: None | str):
        self.customer_id = customer_id
        self.name = name
        self.address = address
