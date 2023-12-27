number = int(input('Enter a number or end the sequence: '))
max_global = 0
max_cur = 0

while number != -1:
    if number != 0:
        if number > max_cur:
            max_cur = number
    else:
        print('Maximum element of current sequence: ', max_cur, '\n')
        if max_cur > max_global:
            max_global = max_cur
        max_cur = 0

    number = int(input('Enter a number or end the sequence: '))

print('Maximum element of all sequences: ', max_global)


