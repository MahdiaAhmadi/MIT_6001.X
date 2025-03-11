def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
    '''
    # Your code 
    invert_dict={}
    
    for key,value in d.items():
       if value not in invert_dict:
           invert_dict[value]=[key]
       else:
           invert_dict[value].append(key)

    for key in invert_dict:
        invert_dict[key].sort() 
           
    return invert_dict
     
print(dict_invert({8: 6, 2: 6, 4: 6, 6: 6}))
