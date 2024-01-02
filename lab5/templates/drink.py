from templates.dish import Dish


class Drink(Dish):
    def __init__(self, id, price, alcohol):
        super().__init__(id, price)
        self.alcohol = alcohol
