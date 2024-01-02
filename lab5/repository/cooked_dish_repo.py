from repository.data_repo import DataRepo
from templates.cooked_dish import CookedDish


class CookedDishRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

