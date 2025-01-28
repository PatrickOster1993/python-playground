from Address import Address
from Customer import Customer
class Bank:
    address: Address
    __customers : list[Customer] = None
    def __init__(self, name: str, registered_address: Address, swift_code: str, logo: str = None):
        self.name = name
        self.address = registered_address
        self.swift_code = swift_code
        self.logo = logo
        self.has_online_banking = False

    def setCustomer(self, customer: Customer):
        if self.__customers is None:
            self.__customers = []
        self.__customers.append(customer)

    def allCustomers(self) -> list[Customer]:
        return self.__customers
    
    def getCustomer(self, customer_id: str) -> Customer:
        for customer in self.__customers:
            if customer.customer_id == customer_id:
                return customer
        return None
