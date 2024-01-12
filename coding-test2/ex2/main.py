from ex2.creditBankAccount import CreditBankAccount


def main():
    firstAccount = CreditBankAccount("owner1")
    secondAccount = CreditBankAccount("owner2")

    firstAccount.amount = 100
    secondAccount.amount = 50
    secondAccount.withdraw(1000)

    thirdAccount = firstAccount + secondAccount
    print(thirdAccount)


main()
