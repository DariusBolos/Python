from repository.data_repo import DataRepo


class OrderRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/order.dat'
