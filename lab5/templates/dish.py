from templates.identifiable import Identifiable


class Dish(Identifiable):
    portionSize = 350

    def __init__(self, id, price):
        super().__init__(id)
        self.price = price
