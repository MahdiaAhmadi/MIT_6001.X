
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    result=[]
    for chars in aList:
        if len(chars) < 4:
            result.append(chars)
    return result
    
print(lessThan4(["apple", "cat", "dog", "banana"])) # return ['cat','dog']

