def number_to_the_power_of(number, power):
    value = 1
    while power:
        value *= number
        power -= 1
    return value


num = float(input('Enter the number: '))
pow = int(input('Enter the power: '))

print(number_to_the_power_of(num, pow))