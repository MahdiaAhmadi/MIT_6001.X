


def isIn(char,aStr):
    '''
    char: a single character
    aStr: a alphabetized String

    returns: True if char is in aStr; False otherwise
    
    '''
    if aStr == '':  # Base case: If string is empty, return False
        return False

    midIndex = len(aStr) // 2  # Find the middle index
    midChar = aStr[midIndex]  # Get the middle character

    if char == midChar:  # If the character matches, return True
        return True
    elif char < midChar:  # If char is smaller, search the left half
        return isIn(char, aStr[:midIndex])
    else:  # If char is greater, search the right half
        return isIn(char, aStr[midIndex + 1:])
        
print(isIn('c', 'abcdefghijklmopqrstuvwxyz'))  


