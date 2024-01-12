from ex2.bankAccount import BankAccount


class CreditBankAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.creditScore = 1

    def withdraw(self, amountToWithdraw):
        try:
            self.amount = super().withdraw(amountToWithdraw)
            self.creditScore += 1
        except:
            self.creditScore -= 1

    def __add__(self, other):
        newInstance = CreditBankAccount(self.owner)

        newInstance.amount = self.amount + other.amount
        newInstance.creditScore = self.creditScore + other.creditScore

        return newInstance

    def __str__(self):
        return f"Account owner: {self.owner}, Amount Left: {self.amount}, Credit Score: {self.creditScore}"
