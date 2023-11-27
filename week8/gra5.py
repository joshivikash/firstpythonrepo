def equality(P, Q):
    size = len(P)
    for i in range(size):
        if P[i] != Q[i]:
            return False
    return True

print(equality([1,2,3],[1,2]))