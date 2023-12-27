def is_prime(number):
    if number == 2:
        return True

    if number < 2 or number % 2 == 0:
        return False

    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True


def sum_prime_divisors(number):
    if is_prime(2) and is_prime(number - 2):
        return 2, number - 2

    for factor in range(3, number, 2):
        if is_prime(factor) and is_prime(number - factor):
            return factor, number - factor

    return False


value = int(input('Enter value for a number: '))
print(sum_prime_divisors(value))
