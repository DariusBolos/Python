from repository.data_repo import DataRepo


class CustomerRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)
