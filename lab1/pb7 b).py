def belongs_to_interval(number, lowerMargin, upperMargin):
    if number >= lowerMargin and number <= upperMargin:
        return True
    return False

max_length = 0
cur_length = 0

arrLength = int(input('Enter the length of the array: '))
lower = int(input('Enter the value of the lower margin of the interval: '))
upper = int(input('Enter the value of the upper margin of the interval: '))
arr = [int(input()) for ind in range(arrLength)]

for index in range(arrLength):
    if belongs_to_interval(arr[index], lower, upper):
        cur_length += 1
    else:
        if(cur_length > max_length):
            max_length = cur_length
        cur_length = 0

if(cur_length > max_length):
            max_length = cur_length

print(max_length)