import random


class Identifiable:
    def __init__(self, id):
        if type(id) is str:
            self.id = id
        else:
            self.id = random.randint(1, 1000)

