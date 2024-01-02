def defaultInterface():
    dict = {

    }

    while True:
        print("""
        Welcome to the best Restaurant press the following keys to continue:
            1 - Menu
            2 - Customers
            3 - Order
            0 - exit 
        """)

        value = int(input())

        if value == 0:
            break


def menuInterface():
    while True:
        value = int(input(("""
        Select an option available in the menu section:
            1 - View the menu
            2 - Search for an item in the menu
            3 - Add a new menu item
            4 - Update an existing menu item 
            5 - Delete an existing menu item
            0 - back        
        """)))
