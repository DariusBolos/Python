# Call every main function, using function_numberOfFunction (1-7)
# I know it's not a good coding practice, but it makes figuring out which function to call easier...

def function_1(numberList):  # returns the array with unique elements
    dict = {}
    for value in numberList:
        dict[value] = 1

    arr = []
    for key in dict:
        arr.append(key)

    return arr


def mirrored_value_2(number):  # returns the mirrored value of a number
    value = 0
    while number > 0:
        value = value * 10 + (number % 10)
        number //= 10

    return value


def function_2(numberList):  # returns the number of symmetrical (xy, yx) pair of numbers
    dict = {}
    for value in numberList:
        if (value // 10) > (value % 10):
            try:
                dict[mirrored_value_2(value)] += 1
            except KeyError:
                dict[mirrored_value_2(value)] = 1
        else:
            try:
                dict[value] += 1
            except KeyError:
                dict[value] = 1

    counter = 0
    for key in dict:
        if dict[key] % 2 == 0:
            counter = counter + dict[key] // 2
        else:
            dict[key] -= 1
            counter = counter + dict[key] // 2

    return counter


def merge_sort(arr: list):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        index_left = 0
        index_right = 0
        index_merged = 0
        while index_left < len(left_arr) and index_right < len(right_arr):
            if left_arr[index_left] > right_arr[index_right]:
                arr[index_merged] = left_arr[index_left]
                index_left += 1
            else:
                arr[index_merged] = right_arr[index_right]
                index_right += 1
            index_merged += 1

        while index_left < len(left_arr):
            arr[index_merged] = left_arr[index_left]
            index_left += 1
            index_merged += 1

        while index_right < len(right_arr):
            arr[index_merged] = right_arr[index_right]
            index_right += 1
            index_merged += 1


def function_3(numberList):  # returns the biggest number formed out of the elements of the array
    merge_sort(numberList)
    value = 0
    for elem in numberList:
        value = value * 100 + elem

    return value


def base2_transformation_4(number):  # returns the base 2 representation of a number
    base2_number = 0
    power = 1
    while number > 0:
        rest = number % 2
        number //= 2
        base2_number = power * rest + base2_number
        power *= 10

    return base2_number


def base10_transformation_4(number):  # returns the base 10 representation of a number in binary
    value = 0
    power = 0
    while number:
        value = value + (number % 10) * pow(2, power)
        number //= 10
        power += 1

    return value


def xor_4(number1, number2):  # returns the xor of a number after converting it to base 2
    number1 = str(base2_transformation_4(number1))
    number2 = str(base2_transformation_4(number2))
    arr1 = []
    arr2 = []

    for ch in number1:
        arr1.append(ch)

    for ch in number2:
        arr2.append(ch)

    if len(arr1) > len(arr2):
        while len(arr2) != len(arr1):
            arr2.insert(0, '0')

    if len(arr1) < len(arr2):
        while len(arr1) != len(arr2):
            arr1.insert(0, '0')

    value = 0
    for index in range(0, len(arr1)):
        if arr1[index] == arr2[index]:
            value *= 10
        else:
            value = value * 10 + 1

    return value


def xor_encoding_4(numberList):  # performs the xor of every element and the first value of the array
    for index in range(1, len(numberList)):
        numberList[index] = base10_transformation_4(xor_4(numberList[0], numberList[index]))


def sum_encoding_4(numberList: list):  # encodes every value by adding the first element of the list to it
    for index in range(1, len(numberList)):
        numberList[index] += numberList[0]


def multiplication_encoding_4(numberList: list):  # encodes every value by multiplying
    for index in range(1, len(numberList)):  # the first element of the list to it
        numberList[index] *= numberList[0]


def sum_decoding_4(numberList: list):  # decodes every value by subtracting the first value of the list from it
    for index in range(1, len(numberList)):
        numberList[index] -= numberList[0]


def multiplication_decoding_4(numberList: list):  # decodes every value by dividing the first value of the list to it
    for index in range(1, len(numberList)):
        numberList[index] //= numberList[0]


def function_4(arr):  # realizes the encoding and decoding of every value by using a menu and prints the final array
    encoded = False
    while True:
        print("""
        1 - add
        2 - multiply
        3 - xor
        0 - exit
        """)

        value = input('Choose an option from the menu: ')
        if value == 0:
            break

        if not encoded:
            option = {
                '1': sum_encoding_4,
                '2': multiplication_encoding_4,
                '3': xor_encoding_4,
            }
            encoded = True
            option[value](arr)
            print(arr)
        else:
            while encoded:
                print("""
                List has already been encoded, please decode first: 
                1 - subtract
                2 - divide
                3 - xor
                0 - exit
                """)

                value = input('Choose an option from the menu: ')
                if value == 0:
                    break

                option = {
                    '1': sum_decoding_4,
                    '2': multiplication_decoding_4,
                    '3': xor_encoding_4,
                }

                encoded = False
                option[value](arr)
                print(arr)


def evaluate_expresion_5(string, value1, value2):  # evaluates a given expresion with two numbers from the array
    exp1 = str(value1)
    exp2 = str(value2)
    expresion = string.replace("x", exp1)
    expresion = expresion.replace("y", exp2)

    arr = expresion.split('=')

    if eval(arr[0]) == eval(arr[1]):
        return True
    return False


def function_5(operation, numberList):  # prints every pair of elements that satisfy the given condition
    for ind1 in range(len(numberList) - 1):
        for ind2 in range(ind1 + 1, len(numberList)):
            if evaluate_expresion_5(operation, numberList[ind1], numberList[ind2]):
                print(numberList[ind1], numberList[ind2], sep=" ")


def is_domino_6(number1, number2):  # verifies if a numbers first digit is the same as the second number's last digit
    return number2 // 10 == number1 % 10


def function_6(numberList):  # returns the longest sequence of numbers that have the first digit equal to
    final_list = []  # the next value's last digit
    current_list = []
    length = 1
    max_length = 0
    for ind in range(1, len(numberList)):
        if is_domino_6(numberList[ind - 1], numberList[ind]):
            current_list.append(numberList[ind - 1])
            length += 1
        else:
            if length > max_length:
                max_length = length
                length = 1
                final_list = [*current_list, numberList[ind - 1]]
                current_list.clear()

    if length > max_length:
        final_list = [*current_list, numberList[len(numberList) - 1]]

    return final_list


def greatest_common_divisor_7(number1, number2):  # returns the greatest common divisor of two numbers
    if number2 != 0:
        return greatest_common_divisor_7(number2, number1 % number2)
    return number1


def function_7(numberList):  # returns the smallest common multiple of every element in the list
    start = int(input('Enter a lower margin: '))
    stop = int(input('Enter an upper margin: '))
    current_number = numberList[start]
    smallest_common_multiple = 0
    for index in range(start + 1, stop + 1):
        smallest_common_multiple = (current_number // greatest_common_divisor_7(current_number, numberList[index])
                                    * numberList[index])
        current_number = smallest_common_multiple

    return smallest_common_multiple


def main():  # simple main function where we read the length and values in the list
    arr = [22, 31, 54, 12, 72, 47, 48, 45, 26, 66]

    print(function_3(arr))


main()
