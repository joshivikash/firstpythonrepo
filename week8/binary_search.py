import random
def binary_search(L, e):
    if len(L) == 1:
        return e == L[0]
    elif len(L) == 0:
        return False
    i = len(L) // 2 - 1 # since index starts from 0
    if len(L) % 2 != 0:
        i = i + 1
    if L[i] == e:
        return True
    elif L[i] > e:
        return binary_search(L[:i], e)
    else:
        return binary_search(L[i+1:], e)
    
L = random.sample(range(100), 10)
L.sort()
print('List {}'.format(L))
present = binary_search(L, 50)
print(present)