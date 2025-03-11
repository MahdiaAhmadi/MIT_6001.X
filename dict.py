

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    max_key=None
    max_length=0
    for keys,values in aDict.items():
        if len(values)> max_length:
            max_key=keys
            max_length=len(values)
    return max_key

    
print(how_many({ 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],'d':['donkey','dog','dingo']}))