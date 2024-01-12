class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.amount = 0

    def withdraw(self, amountToWithdraw):
        if amountToWithdraw > self.amount:
            raise Exception("NoMoney")
        else:
            return self.amount - amountToWithdraw
