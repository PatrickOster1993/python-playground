from Account import Account
from Customer import Customer
from Bank import Bank

myCustomer = Customer("John Doe", "123 Main St", "12345")
#print (f"Customer   Address: {myCustomer.address} Name: {myCustomer.name} ID: {myCustomer.customer_id}")

trump = Customer("Donald Trump", "1600 Pennsylvania Ave", "00001")
#print (f"Customer   Address: {trump.address} Name: {trump.name} ID: {trump.customer_id}")


myBank = Bank("Bank of America", "123 Wall St", "BOFAUS3N")
#print (f"Bank  Address: {myBank.address} Name: {myBank.name} Swift Code: {myBank.swift_code}")

myBank.setCustomer(trump)
myBank.setCustomer(myCustomer)


kundeList = myBank.allCustomers()

for customer in kundeList:
    print (f"Customer   Address: {customer.address} Name: {customer.name} ID: {customer.customer_id}")