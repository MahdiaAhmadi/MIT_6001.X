'''
def iterPower(base, exp):
    
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
   
    result=1
    while exp > 0:
       result *= base
       exp-=1
    return result

print(iterPower(2,4))'''



def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp <=0:
        return 1
    else:
        return base * recurPower(base,exp-1)
    
print(recurPower(2,4))









