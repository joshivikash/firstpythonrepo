def count(L, word):
    """
    A recursive function to compute the frequency of occurrences of word in L

    Arguments:
        L: list of words
        word: string
    Return:
        result: integer
    """
    if len(L) == 0:
        return 0
    elif L.pop() == word:
        return 1 + count(L, word)
    else:
        return 0 + count(L, word)
    
print(count(['a','b','a'], 'a'))