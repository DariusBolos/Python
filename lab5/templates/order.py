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

    def __generateInvoice(self):
        self.calculateCosts()
        dishList = dishManager.load()
        drinkList = drinkManager.load()
        invoice = f"Order: {self.id} for the customer with id: {self.customerId}" + '\n'

        names = []
        prices = []

        for dish in dishList:
            if dish.id in self.dishes:
                names.append(dish.id)
                prices.append(str(dish.price))

        for drink in drinkList:
            if drink.id in self.drinks:
                names.append(drink.id)
                prices.append(str(drink.price))

        items = list(map(lambda x, y: f"Item: {x}     Price: {y} Euro" + '\n', names, prices))

        invoice += "".join(items)
        invoice += f"Total: {str(self.total)} Euro"

        return invoice

    def displayInvoice(self):
        invoice = self.__generateInvoice()
        print(invoice)

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return f'Order: {self.id}   Customer: {self.customerId}   Dishes: {self.dishes}   Drinks: {self.drinks}'
