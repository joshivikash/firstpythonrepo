def linear(P, Q, k):
    """
    A recursive function to determine if a list is scalar multiple of the other

    Arguments:
        P: list of integers
        Q: list of integers
        k: integer
    Return:
        result: bool
    """
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    print('P[-1] = {}'.format(P[-1]))
    print('Q[-1] * k = {}'.format(Q[-1] * k))
    return P[-1] == (Q[-1] * k) and linear(P[:-1],Q[:-1], k)

print(linear([2,4,6],[1,2,3],2))