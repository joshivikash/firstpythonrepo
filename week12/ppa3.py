def survival(T):
    """
    Determine if the organism will survive or not
    
    Argument:
        T: integer
    Return:
        result: bool
    """
    for t in {34, 24, 25, 26, 27, 28, 30, 31} :
        if t <= T:
            return True
    return False