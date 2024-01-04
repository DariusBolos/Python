from repository.data_repo import DataRepo


class DrinkRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/drink.dat'
