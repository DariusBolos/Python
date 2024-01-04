from repository.customer_repo import CustomerRepo
from controller.data_logic import displayData
from templates.customer import Customer

customerManager = CustomerRepo()


def getAllCustomers():
    print("Customers: ")
    displayData(2)


def addCustomer():
    name = input("Name of the customer: ")
    address = input("Address of the customer: ")

    customers = customerManager.load() if customerManager.load() else []
    customer = Customer(1, name, address)
    customers.append(customer)
    customerManager.sort(customers)


def updateCustomer():
    getAllCustomers()
    listID = int(input("Enter the id of the item you would like to update: "))
    customers = customerManager.load()

    id = customers[listID].id
    name = input("Enter the new name of the customer: ")
    address = input("Enter the new address of the customer: ")
    customer = Customer(id, name, address)
    customerManager.update(listID, customer)


def deleteCustomer():
    getAllCustomers()
    id = int(input("Enter the id of the customer you would like to delete: "))
    customerManager.remove(id)
