from repository.cooked_dish_repo import CookedDishRepo
from repository.drink_repo import DrinkRepo
from templates.cooked_dish import CookedDish
from templates.drink import Drink
from controller.data_logic import displayData

dishManager = CookedDishRepo()
drinkManager = DrinkRepo()


def displayMenu():  # displays all dishes and drinks
    print("Dishes: ")
    displayData(0)

    print("Drinks: ")
    displayData(1)


def addDish():  # adds a new dish
    name = input("Name of the dish: ")
    price = int(input("Price of the dish: "))
    prepTime = int(input("Estimated preparation time of the dish: "))

    dishes = dishManager.load() if dishManager.load() else []
    dish = CookedDish(name, price, prepTime)
    dishes.append(dish)
    dishManager.sort(dishes)


def addDrink():  # adds a new dish
    name = input("Name of the drink: ")
    price = int(input("Price of the drink: "))
    alcohol = input("Alcohol percentage in the drink: ")

    drinks = drinkManager.load() if drinkManager.load() else []
    drink = Drink(name, price, alcohol)
    drinks.append(drink)
    drinkManager.sort(drinks)


def searchItem():  # lets the user search for an item
    name = input("Enter the name of the item you would like to search: ")
    dishes = dishManager.load() if dishManager.load() else []
    drinks = drinkManager.load() if drinkManager.load() else []
    print('\n')
    if dishes:
        print("Dishes: ", '\n')
        for index in range(len(dishes)):
            if name.lower() in dishes[index].id.lower():
                print(index, str(dishes[index]))

    if drinks:
        print("Drinks: ", '\n')
        for index in range(len(drinks)):
            if name.lower() in drinks[index].id.lower():
                print(index, str(drinks[index]))

        return

    print("No items found that include the given name")


def updateItem():  # updates an item from the menu
    type = int(input("""
    Enter the type of the item you would like to update: 
        1 - Dish
        2 - Drink
    """))

    id = int(input("Enter the id of the item you would like to update: "))

    if type == 1:
        name = input("Enter the new name of the dish: ")
        price = input("Enter the new price of the dish: ")
        prepTime = input("Enter the new preparation time of the dish: ")
        dish = CookedDish(name, price, prepTime)
        dishManager.update(id, dish)
    else:
        name = input("Enter the new name of the drink: ")
        price = input("Enter the new price of the drink: ")
        alcohol = input("Enter the new alcohol percentage of the drink: ")
        drink = Drink(name, price, alcohol)
        drinkManager.update(id, drink)


def showMenuUpdate():
    displayMenu()
    updateItem()


def deleteItem():  # deletes an item from the menu
    type = int(input("""
        Enter the type of the item you would like to delete: 
            1 - Dish
            2 - Drink
        """))

    id = int(input("Enter the id of the item you would like to delete: "))

    if type == 1:
        dishManager.remove(id)
    else:
        drinkManager.remove(id)


def showMenuDelete():
    displayMenu()
    deleteItem()
