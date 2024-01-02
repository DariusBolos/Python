from templates.identifiable import Identifiable


class Dish(Identifiable):
    portionSize = 350

    def __init__(self, id, price):
        super().__init__(id)
        self.price = price

    def __new__(cls):
        raise Exception("Class is intended as an abstract class")
