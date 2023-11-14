def search(L, k):
    """
    A recursive function that searches for an element k in L

    Arguments:
    	L: list
    	k: int
    Return:
    	bool
    """
    if len(L) == 1:
        return L[0] == k
    elif search(L[1:], k) or L[0] == k:
        return True
    else:
        return False