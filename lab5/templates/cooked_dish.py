from templates.dish import Dish


class CookedDish(Dish):
    def __init__(self, id, price, prepTime):
        super().__init__(id, price)
        self.prepTime = prepTime

    def __lt__(self, other):  # redefining the lower than function, helpful by object comparison
        return self.id < other.id

    def __iter__(self):
        return iter(self.id, self.price)

    def __str__(self):
        return f'{self.id}    {self.price} Euro    {self.prepTime} Minutes'
