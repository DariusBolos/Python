from repository.data_repo import DataRepo


class CustomerRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/customer.dat'
