from models.identifiable import Identifiable


class Customer(Identifiable):
    def __init__(self, id, name, address):
        super().__init__(id)
        self.name = name
        self.address = address
