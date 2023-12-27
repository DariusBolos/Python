from models.dish import Dish


class CookedDish(Dish):
    def __init__(self, id, name, price, prepTime):
        super().__init__(id, name, price)
        self.prepTime = prepTime
