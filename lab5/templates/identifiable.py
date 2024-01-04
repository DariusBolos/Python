class Identifiable:
    count = 0

    def __init__(self, id):
        if type(id) is str:
            self.id = id
        else:
            self.id = self.count
            Identifiable.count += 1
