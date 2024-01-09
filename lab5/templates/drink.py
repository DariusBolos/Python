from templates.dish import Dish


class Drink(Dish):
    def __init__(self, id, price, alcohol):
        super().__init__(id, price)
        self.alcohol = alcohol

    def __lt__(self, other):  # redefining the lower than function, helpful by object comparison
        return self.id < other.id

    def __iter__(self):
        return iter(self.id, self.price)

    def __str__(self):
        return f'{self.id}    {self.price} Euro    {self.alcohol}% alcohol'
