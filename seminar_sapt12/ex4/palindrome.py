from math import log10

def is_palindrome(number):
    if number <= 10:
        return True
    
    if(number // (10 ** (int(log10(number)) + 1) - 1) != number % 10):
        return False
    
    return is_palindrome(number % 10 ** int(log10(number)) // 10)
