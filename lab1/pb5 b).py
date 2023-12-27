from numpy import *


def greatest_common_divisor(number1, number2):
    if number2 != 0:
        return greatest_common_divisor(number2, number1 % number2)
    return number1

# returns the greatest common divisor of two numbers


def longest_sequence(arr: list):
    max_len, cur_len = 0, 1
    cur_arr, final_arr = [], []

    for index in range(1, len(arr)):
        if greatest_common_divisor(arr[index], arr[index - 1]) == 1:
            cur_len += 1
            cur_arr.append(arr[index - 1])
        else:
            cur_arr.append(arr[index - 1])
            if cur_len > max_len:
                max_len = cur_len
                final_arr = cur_arr.copy()
            cur_arr.clear()
            cur_len = 1

    if cur_len > max_len:
        cur_arr.append(arr[len(arr) - 1])
        max_len = cur_len
        final_arr = cur_arr.copy()

    return final_arr, max_len

# returns the final subsequence of one between other prime numbers and its length


def main():
    arr_length = int(input('Enter length of array: '))
    arr = [int(input()) for ind in range(arr_length)]

    (final_list, list_length) = longest_sequence(arr)
    print(f"The longest sequence is {final_list} and it has the length of: {list_length}")


main()
