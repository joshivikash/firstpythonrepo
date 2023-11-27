def collatz(n):
    """
    A recursive function to compute the number of calls to the Collatz function of n

    Argument:
        n: integer
        Assume that 1 < n <= 32,000
    Returns: 
        result: integer
    """
    if n % 2 == 0 and n // 2 == 1:
        return 1
    elif n % 2 != 0 :
        return 1 + collatz((3 * n) + 1)
    else:
        return 1 + collatz(n // 2)