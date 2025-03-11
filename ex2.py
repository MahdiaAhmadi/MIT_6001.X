

'''Write an iterative function, gcdIter(a, b), that implements this idea. 
One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, 
and iteratively reduce this test value by 1 until you either reach a case where the test divides both a 
and b without remainder, or you reach 1.'''


def gcdIter(a,b):

    testvalue=min(a,b)
    while a%testvalue!=0 or b%testvalue!=0:
        testvalue -=1
    return testvalue
   

print(gcdIter(9, 12))



def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
     return a
    else:
        return gcdRecur(b, a % b)
    
print(gcdRecur(9,12))