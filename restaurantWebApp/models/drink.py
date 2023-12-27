from models.dish import Dish


class Drink(Dish):
    def __init__(self, id, name, price, alcohol):
        super().__init__(id, name, price)
        self.alcohol = alcohol
