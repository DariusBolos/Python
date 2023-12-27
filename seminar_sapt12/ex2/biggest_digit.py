def last_big_digit(string):
    if len(string) == 0:
        return None
    
    if(string[-1].isupper()):
        return string[-1]
    
    return last_big_digit(string[0 : len(string) - 1])