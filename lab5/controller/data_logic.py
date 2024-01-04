from repository.cooked_dish_repo import CookedDishRepo
from repository.drink_repo import DrinkRepo
from repository.customer_repo import CustomerRepo
from repository.order_repo import OrderRepo


def displayData(repoType):
    types = {
        0: CookedDishRepo,
        1: DrinkRepo,
        2: CustomerRepo,
        3: OrderRepo
    }

    repo = types[repoType]()

    list = repo.load()
    if list:
        for index in range(len(list)):
            print(index, str(list[index]))
    print('\n')
