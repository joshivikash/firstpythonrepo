def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    M_ij = []
    for x in range(len(M)):
        row = []
        for y in range(len(M[0])):
            if x == i or y == j:
                continue
            row.append(M[x][y])
        if len(row) > 0:
            M_ij.append(row)
    return M_ij

M = [[1,2,3],[4,5,6],[7,8,9]]
print(minor_matrix(M,0,0))
# 1 2 3
# 4 5 6
# 7 8 9

#
#  5 6
#  8 9