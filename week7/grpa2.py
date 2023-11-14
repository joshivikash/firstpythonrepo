def merge(D1, D2, priority):
    """
    Merge two dicts

    Arguments: 
        - D1: first dictionary
        - D2: second dictionary
        - priority: string
    Returns: D; merged dictionary
    """
    D = {}
    for key1 in D1:
        for key2 in D2:
            if key1 == key2:
                if priority == 'first':
                    D[key1] = D1[key1]
                else:
                    D[key1] = D2[key1]
            elif key2 not in D:
                D[key2] = D2[key2]
        if key1 not in D:
            D[key1] = D1[key1]
    return D