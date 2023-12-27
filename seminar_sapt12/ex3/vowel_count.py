def count(string):
    if not len(string):
        return 0
    
    if(string[-1] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
        return 1 + count(string[0 : len(string) - 1])
    
    return count(string[0 : len(string) - 1])