def spiral_iterative(left, right, n):
    """
    An iterative function to compute the x-coordinate of the nth arm of the spiral

    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    for i in range(1,n+1):
        if i%2 == 0:
            right = (right + left)/2
        else:
            left = (right + left)/2
    if i % 2 == 0:
        return left
    else:
        return right
    
def spiral_recursive(left, right, n):
    """
    An recursive function to compute the x-coordinate of the nth arm of the spiral

    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    if n == 1:
        return right
    if n % 2 == 0:
        mid_point = (right + left)/2
        n = n - 1
        return spiral_recursive(mid_point, right, n) 
    else:
        mid_point = (right + left)/2
        n = n - 1
        return spiral_recursive(left, mid_point,  n)
    

print(spiral_iterative(0,1,4))
print(spiral_recursive(0,1,4))