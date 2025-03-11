def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    for example:
    def f(i):
    return i + 2
    def g(i):
    return i > 5

    L = [0, -10, 5, 6, -4]
    print(applyF_filterG(L, f, g))
    print(L)
    Should print:
    6
    [5, 6]
    """
    # Your code here

    i = 0
    while i < len(L):
        if not g(f(L[i])):  # Check the condition for the current element
            L.pop(i)  # Remove the element if it does not satisfy the condition
        else:
            i += 1  
    return max(L,default=-1)

def f(i):
    return i+2

def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L,f,g))
print(L)



