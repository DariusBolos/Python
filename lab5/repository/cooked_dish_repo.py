from repository.data_repo import DataRepo


class CookedDishRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/cooked_dish.dat'

