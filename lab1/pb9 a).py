def prime_factorization(number):
    div = 2
    pow = 0
    while number > 1:
        pow = 0
        while number % div == 0:
            pow += 1
            number /= div

        if pow:
            print(str(div) + ': ' + str(pow) + '\n')

        div += 1

        if div * div > number:
            div = number


num = int(input('Number to be factorized: '))
print(prime_factorization(num))