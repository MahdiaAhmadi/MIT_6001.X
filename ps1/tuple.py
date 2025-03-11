
#solution 1
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
   '''
    oddTuples=()
    for i in range(0,len(aTup),2):
        oddTuples += (aTup[i],)
    return oddTuples

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))



#solution 2
def oddTuples2(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]
