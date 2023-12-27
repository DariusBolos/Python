def equal_digits (number):
    string = str(number)
    dict = {}
    for ch in string:
        dict[ch] = 1

    return dict

arrLength = int(input('Enter length of array: '))
arr = [int(input()) for ind in range(arrLength)]
maxLength = 0
curLength = 1

for iterator in range (1, arrLength):
    if equal_digits(arr[iterator - 1]) == equal_digits(arr[iterator]):
        curLength += 1
    else:
        if curLength > maxLength:
            maxLength = curLength
        curLength = 1

if curLength > maxLength:
    maxLength = curLength

print(maxLength)