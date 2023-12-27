def is_prime(number: int):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True  # prime number function


def longest_sequence(numberList):
    seq = 0
    seq_max = 0
    cur_array = []
    final_array = []

    for index in range(len(numberList)):
        if is_prime(numberList[index]):
            seq = seq + 1
            cur_array.append(numberList[index])
        else:
            if seq > seq_max:
                final_array = [*cur_array]
                seq_max = seq
            cur_array.clear()
            seq = 0

    if seq > seq_max:
        final_array = [*cur_array]

    return final_array  # returns the longest sequence of prime numbers


def main():
    arrLength = int(input("Length of array: "))
    arr = [int(input()) for i in range(arrLength)]
    print(longest_sequence(arr))


main()
