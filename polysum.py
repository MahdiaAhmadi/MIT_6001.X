

import math

def polySum(n, s):
    '''
    n: int, number of sides of the polygon
    s: float, length of each side
    
    returns: float, sum of the area and square of the perimeter, rounded to 4 decimal places
    '''
    # Calculate area of the polygon
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    
    # Calculate perimeter of the polygon
    perimeter = n * s
    
    # Calculate sum of area and square of perimeter
    result = area + perimeter**2
    
    # Return result rounded to 4 decimal places
    return round(result, 4)

# Example usage
print(polySum(5, 3))  # Example test case
