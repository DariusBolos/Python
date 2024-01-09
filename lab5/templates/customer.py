from templates.identifiable import Identifiable


class Customer(Identifiable):
    def __init__(self, id, name, address):
        super().__init__(id)
        self.name = name
        self.address = address

    def __lt__(self, other):  # redefining the lower than function, helpful by object comparison
        return self.name < other.name

    def __str__(self):
        return f'{self.id}   {self.name}   {self.address}'
