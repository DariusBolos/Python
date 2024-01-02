from templates.dish import Dish


class CookedDish(Dish):
    def __init__(self, id, price, prepTime):
        super().__init__(id, price)
        self.prepTime = prepTime
