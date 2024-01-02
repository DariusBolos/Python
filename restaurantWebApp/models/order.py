from models.identifiable import Identifiable
from flask_sqlalchemy import SQLAlchemy
from data.models.tables import CookedDishTable, DrinkTable


class Order(Identifiable):
    def __init__(self, id, customerId, dishIds, drinkIds, total):
        super().__init__(id)
        self.customerId = customerId
        self.dishIds = dishIds
        self.drinkIds = drinkIds
        self.total = total

    def calculateCostsDB(self):
        dishes = CookedDish.query.all()
        drinks = DrinkTable.query.all()
        totalCosts = []
        for dish in dishes:
            if dish.id in self.dishIds:
                totalCosts.append(dish.price)

        for drink in drinks:
            if drink.id in self.drinkIds:
                totalCosts.append(drink.price)

        self.total = reduce(lambda x, y: x + y, totalCosts)

    def __generateReceipt__(self):
        pass
