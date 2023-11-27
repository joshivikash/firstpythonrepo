def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of person

    Arguments:
        P: dict, key and value are strings
        present: string
        past: string
    Return:
        result: list of strings
    """
    if P[present] == past:
        return [present,past]
    else:
        return [present] + ancestry(P, P[present], past)
    
print(ancestry({'Anil': 'Krishna', 'Mohan': 'Prasanna', 'Krishna': 'Prasanna', 'Prasanna': 'Mukesh'}, 'Anil', 'Prasanna'))