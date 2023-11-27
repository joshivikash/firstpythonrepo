def mini(L):
    minimum = L[0]
    for e in L:
        if e < minimum:
            minimum = e
    return minimum

def sort(L):
    if len(L) == 0 or len(L) == 1:
        return L
    m = mini(L)
    L.remove(m)
    return [m] + sort(L)

print(sort([3,43,2,676,1,9,2,10,6,87]))