from templates.identifiable import Identifiable
from controller.menu_logic import dishManager, drinkManager
from functools import reduce


class Order(Identifiable):
    total = 0

    def __init__(self, id, customerId, dishes, drinks):
        super().__init__(id)
        self.customerId = customerId
        self.dishes = dishes
        self.drinks = drinks

    def calculateCosts(self):
        dishList = dishManager.load()
        drinkList = drinkManager.load()
        prices = []

        for dish in dishList:
            if dish.id in self.dishes:
                prices.append(int(dish.price))

        for drink in drinkList:
            if drink.id in self.drinks:
                prices.append(int(drink.price))

        self.total = reduce(lambda x, y: x + y, prices)

    def __generateInvoice__(self):
        self.calculateCosts()
        dishList = dishManager.load()
        drinkList = drinkManager.load()
        invoice = f"Order: {self.id} for the customer with id {self.customerId} '\n''\n'"

        invoice += f"Dishes: '\n'"

        for dish in dishList:
            invoice += str(dish)

    def __str__(self):
        return f'Order: {self.id}   Customer: {self.customerId}   Dishes: {self.dishes}   Drinks: {self.drinks}'
