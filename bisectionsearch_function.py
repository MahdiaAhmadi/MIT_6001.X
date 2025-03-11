
#iterative approach 

def binary_search(arr,target):
    left,right=0,len(arr)-1

    while left <=right :
        mid= (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left= mid+1
        else:
            right=mid-1
    return -1 #not found
# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")





#Recursive approach

def binary_search_recursive(arr,target,left,right):
    if left > right: # base case
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid+1,right)
    else:
        return binary_search_recursive(arr,target,left,mid-1)
    


# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element found at index: {result}" if result != -1 else "Element not found")





   
    

#Root nth of x 

def nth_root(x, n, precision=1e-6):
    """Finds the nth root of x using bisection search"""
    if x < 0 and n % 2 == 0:
        raise ValueError("Even root of negative number is not real")

    # Define search range
    left, right = (x, 1) if 0 < x < 1 else (0, x)

    while right - left > precision:
        mid = (left + right) / 2  # Find midpoint
        mid_power = mid ** n  # Calculate mid^n

        if abs(mid_power - x) < precision:  # Close enough to x
            return mid
        elif mid_power < x:  # Too small, increase mid
            left = mid
        else:  # Too big, decrease mid
            right = mid

    return (left + right) / 2  # Best estimate of root

# Example usage:
x = 27
n = 3
print(f"The {n}-th root of {x} is approximately {nth_root(x, n)}")

x = 0.008
n = 3
print(f"The {n}-th root of {x} is approximately {nth_root(x, n)}")

        
    

    
