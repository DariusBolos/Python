from models.identifiable import Identifiable


class Dish(Identifiable):
    portionSize = 350

    def __init__(self, id, name, price):
        super().__init__(id)
        self.name = name
        self.price = price

    def __new__(self):
        raise Exception("Class is intended as an abstract class")
