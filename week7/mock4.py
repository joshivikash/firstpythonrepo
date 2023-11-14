def uniq(L):
    """
    A recursive function to get unique elements from the list
    
    Argument:
        L: list
    Return:
        result: list
    """
    if len(L) == 1:
        return [L[0]]
    elif L[0] in uniq(L[1:]):
        L = L[1:]
        return uniq(L)
    else:
        return [L[0]] + uniq(L[1:])
    

print(uniq([1,2,1,4,5,6,1,8,9,1,2,6]))
