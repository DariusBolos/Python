class Identifiable:
    def __init__(self, id):
        self.id = id

    def __new__(self):
        raise Exception("Class is intended as an abstract class")
