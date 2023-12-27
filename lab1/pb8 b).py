def opposite_signs(num1, num2):
    if num1 > num2:
        num1 = num1 + num2
        num2 = num1 - num2
        num1 = num1 - num2

    # a = a + b
    # b = a - b = a + b - b = a
    # a = a - b = a + b - a = b

    if num1 < 0 and num2 >= 0:
        return True

    return False

finalArray = []
finalLength = 0
maxLength = 0

arrayLength = int(input('Length of array: '))
arr = [int(input()) for ind in range(arrayLength)]



