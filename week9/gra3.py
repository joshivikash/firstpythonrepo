from gra2 import get_scores
def do_something(L):
    L.sort()
    mid = len(L) // 2
    if len(L) % 2 == 0:
        return (L[mid] + L[mid - 1]) // 2
    else:
        return L[mid]
    
print(do_something(get_scores('scores.csv', 4)))