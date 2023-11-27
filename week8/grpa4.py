def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps 

    Argument:
        n: integer
    Return:
        result: integer
    """
    if n > 3:
        pass
    elif n == 3:
        return 4
    elif n == 2:
        return 2
    else:
        return 1