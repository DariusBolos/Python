from repository.order_repo import OrderRepo
from repository.customer_repo import CustomerRepo
from controller.customer_logic import getAllCustomers, addCustomer
from controller.menu_logic import drinkManager, dishManager, displayMenu
from controller.data_logic import displayData
from templates.order import Order

orderManager = OrderRepo()
customerManager = CustomerRepo()


def searchCustomerName():
    name = input("Enter the name of the item you would like to search: ")
    customers = customerManager.load() if customerManager.load() else []
    print('\n')
    ids = []
    if customers:
        print("Customers: ", '\n')
        for index in range(len(customers)):
            if name.lower() in customers[index].name.lower():
                print(index, str(customers[index]))
                ids.append(customers[index].id)


def searchCustomerAddress():
    address = input("Enter the name of the item you would like to search: ")
    customers = customerManager.load() if customerManager.load() else []
    print('\n')
    if customers:
        print("Customers: ", '\n')
        for index in range(len(customers)):
            if address.lower() in customers[index].address.lower():
                print(index, str(customers[index]))


def addUserOrder():
    print('\n', "Customers:")
    displayData(2)
    addCustomer()


def newOrder():
    value = int(input("Enter the id of the customer you would like to assign the order to: "))
    customers = customerManager.load() if customerManager.load() else []
    customer = customers[value]

    dishIds = []
    drinkIds = []
    dishes = dishManager.load() if dishManager.load() else []
    drinks = drinkManager.load() if drinkManager.load() else []

    print("Select the items you would like to assign to the order, press -1 to proceed to the order: ", '\n')
    displayMenu()

    while True:
        type = int(input("""
        Enter the id of the item you would like to add:
            1 - Select a cooked dish
            2 - Select a drink 
        """))

        if type == -1:
            break

        if type == 1:
            id = int(input("ID: "))
            if id < len(dishes):
                dishIds.append(dishes[id].id)
            else:
                print("ID not found")
        else:
            id = int(input("ID: "))
            if id < len(drinks):
                drinkIds.append(drinks[id].id)
            else:
                print("ID not found")

    order = Order(1, customer.id, dishIds, drinkIds)
    orders = orderManager.load() if orderManager.load() else []
    orders.append(order)
    orderManager.sort(orders)

    order.displayInvoice()


def displayOrders():
    print("Orders: ")
    displayData(3)

    orders = orderManager.load()
    value = int(input("Enter the id of the order you would like to display the invoice for: "'\n'))
    orders[value].displayInvoice()


