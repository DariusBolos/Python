from repository.cooked_dish_repo import CookedDishRepo
from repository.drink_repo import DrinkRepo
from repository.customer_repo import CustomerRepo
from repository.order_repo import OrderRepo


def displayData(repoType):
    dataPaths = ['repository/data/cooked_dish.dat', 'repository/data/drink.dat', 'repository/data/customer.dat',
                 'repository/data/order.dat']
    types = {
        0: CookedDishRepo,
        1: DrinkRepo,
        2: CustomerRepo,
        3: OrderRepo
    }

    repo = types[repoType](dataPaths[repoType])

    list = repo.load()
    for item in list:
        print(item, '\n')
