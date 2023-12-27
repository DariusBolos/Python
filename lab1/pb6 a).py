def digit_counter(number):
    counter = 0
    if number == 0:
        return 1

    while number:
        if number % 10 == 0:
            counter += 1
        number /= 10

    return counter

value = int(input('Enter a value or null: '))
nr_of_null = 0
if value == 0:
    print(digit_counter(value))
else:
    while(value):
        nr_of_null += digit_counter(value)
        value = int(input('Enter a value or null: '))

print(nr_of_null)

