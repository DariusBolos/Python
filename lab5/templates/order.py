from templates.identifiable import Identifiable
from functools import reduce
import os
import json


class Order(Identifiable):
    total = 0

    def __init__(self, id, customerId, dishes, drinks):
        super().__init__(id)
        self.customerId = customerId
        self.dishes = dishes
        self.drinks = drinks

    def calculateCosts(self):
        pass
