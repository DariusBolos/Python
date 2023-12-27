def is_prime(number):
    if (number == 2):
        return True

    if(number < 2 or number % 2 == 0):
        return False

    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True


arrayLength = int(input('Enter length of array: '))
arr = [int(input()) for index in range(arrayLength)]
max_length = 0
cur_length = 1

for iterator in range(1, arrayLength):
    sum = arr[iterator] + arr[iterator - 1]
    if is_prime(sum):
        cur_length += 1
    else:
        if cur_length > max_length:
            max_length = cur_length
        cur_length = 0

if cur_length > max_length:
    max_length = cur_length

print(max_length)


