import pickle
from operator import itemgetter


class DataRepo:
    def __init__(self, filename):
        self.filename = filename

    def save(self, objectList):
        with open(self.filename, 'wb') as file:
            pickle.dump(objectList, file)

    def load(self):
        with open(self.filename, 'rb') as file:
            return pickle.load(file)

    def sort(self, objectList):
        objectList = sorted(objectList, key=itemgetter('id'))
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
            print("Successfully updated the selected item")
            return

        print("Item with the given id was not found in the list")

