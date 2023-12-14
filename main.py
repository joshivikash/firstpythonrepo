# transpose of a n x n matrix

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M))]


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))