
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    exp=0
    while b ** exp <=x :
        exp +=1 
    return exp -1

print(myLog(15,3))
