def sum(number):
    if number == 0:
        return 0
    
    if(number % 2 == 0):
        return number % 10 + sum(number // 10)
    
    return sum(number // 10)


