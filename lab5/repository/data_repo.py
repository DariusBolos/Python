import pickle

# inherited class that manages every repo with crud


class DataRepo:
    def __init__(self):
        self.filename = None

    def save(self, objectList):
        with open(self.filename, 'wb') as file:
            pickle.dump(objectList, file)

    def load(self):
        with open(self.filename, 'rb') as file:
            try:
                return pickle.load(file)
            except EOFError:
                print("No items were found in the database")

    def sort(self, objectList):
        objectList = sorted(objectList)
        self.save(objectList)

    def add(self, obj):
        objectList = self.load()
        objectList.append(obj)
        self.sort(objectList)
        print("Successfully added a new item")

    def remove(self, id):
        objectList = self.load()
        if id < len(objectList):
            objectList.pop(id)
            self.save(objectList)
            print("Item with the given id was successfully removed")
            return

        print("Item with the given id was not found in the list")

    def update(self, id, newObj):
        objectList = self.load()
        if id < len(objectList):
            self.remove(id)
            self.add(newObj)
            return

        print("Item with the given id was not found in the list")
