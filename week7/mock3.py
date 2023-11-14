def non_decreasing(L):
    """
    A recursive function that determines if L is sorted in non-decreasing order

    Argument: 
        L: list of integers
    Return:
        result: bool
    """
    if len(L) == 1:
        return True
    elif non_decreasing(L[1:]) and L[1] >= L[0]:
        return True
    else:
        return False