from controller.menu_logic import displayMenu, addDish, addDrink, searchItem, showMenuUpdate, showMenuDelete
from controller.customer_logic import getAllCustomers, addCustomer, updateCustomer, deleteCustomer
from controller.order_logic import searchCustomerName, searchCustomerAddress, newOrder, displayOrders, addUserOrder


def defaultInterface():  # standard menu interface
    options = {
        1: menuInterface,
        2: customerInterface,
        3: orderInterface
    }

    while True:
        print("""
        Welcome to the best Restaurant press any of the following keys to continue:
            1 - Menu
            2 - Customers
            3 - Order
            0 - Exit 
        """)

        value = int(input())

        if value == 0:
            exit()

        options[value]()


def typeOfItem():  # menu that lets the user select the type of item they would like to add
    value = int(input("""
    Select the type of item you would like to add
        1 - Dish
        2 - Drink
    """))

    options = {
        1: addDish,
        2: addDrink
    }

    options[value]()
    print("Successfully added the item")
    menuInterface()


def menuInterface():  # selects an option from the menu
    while True:
        value = int(input("""
        Select an option available in the menu section:
            1 - View the menu
            2 - Search for an item in the menu
            3 - Add a new item to the menu
            4 - Update an existing menu item 
            5 - Delete an existing menu item
            0 - Back        
        """))

        options = {
            1: displayMenu,
            2: searchItem,
            3: typeOfItem,
            4: showMenuUpdate,
            5: showMenuDelete,
            0: defaultInterface
        }

        options[value]()

        menuInterface()


def customerInterface():  # selects an option from the customer menu
    while True:
        value = int(input("""
           Select an option available in the customer section:
               1 - View all customers
               2 - Add a new customer
               3 - Update an existing customer 
               4 - Delete an existing customer
               0 - Back        
           """))

        options = {
            1: getAllCustomers,
            2: addCustomer,
            3: updateCustomer,
            4: deleteCustomer,
            0: defaultInterface
        }

        options[value]()

        customerInterface()


def orderInterface():  # chooses an option from the order menu
    while True:
        value = int(input("""
           Select an option available in the order section:
               1 - Add a new order
               2 - View previous orders
               0 - Back        
           """))

        options = {
            1: selectCustomerInterface,
            2: displayOrders,
            0: defaultInterface
        }

        options[value]()


def selectCustomerInterface():  # chooses an option when searching for a customer
    value = int(input("""
         Choose an option available from the following options :
            1 - Search for a customer by name
            2 - Search for a customer by address
            3 - Add a new Customer 
            0 - Back
    """))

    options = {
        1: searchCustomerName,
        2: searchCustomerAddress,
        3: addUserOrder,
        0: orderInterface
    }

    options[value]()

    newOrder()
