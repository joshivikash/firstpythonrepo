def check0(L):
    if L[0] == 0:
        return True
    return check0(L[1:])

print(check0([1,2,3,4,5,6,7,8,9,0,0,0]))