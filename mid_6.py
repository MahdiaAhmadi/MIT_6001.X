def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
    is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).
    '''
    flat_list=[]

    for item in aList:
        if isinstance(item,list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5] ))


