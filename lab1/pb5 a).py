def prime_factorization(number, prime_number):
    divisor = 2
    while number > 1:
        power = 0
        while number % divisor == 0:
            power += 1
            number /= divisor

        if divisor == prime_number:
            print(f"Exponent of prime divisor {divisor} is: {power}")
            return

        if divisor == 2:
            divisor += 1
        else:
            divisor += 2

        if divisor * divisor > number:
            divisor = number

    print(f"Exponent of prime divisor {prime_number} is: {0}")
    return


# prints the power of the prime divisor in the prime factorization of a number

def is_prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True


# verifies if a number is prime

def main():
    value = int(input('Enter the number to be factorized: '))
    pr_nr = int(input('Enter a valid prime number: '))
    while not is_prime(pr_nr):
        pr_nr = int(input('Number is not prime, enter a valid prime number: '))

    prime_factorization(value, pr_nr)


main()
