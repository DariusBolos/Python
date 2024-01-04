from templates.dish import Dish


class CookedDish(Dish):
    def __init__(self, id, price, prepTime):
        super().__init__(id, price)
        self.prepTime = prepTime

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return f'{self.id}    {self.price} Euro    {self.prepTime} Minutes'
