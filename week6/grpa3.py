# CODE WITH ALGORITHM
# (1) First get the transpose of the matrix.
#   (1.1) To get the transpose of a mxn matrix, create a nxm matrix.
#   (1.2) The ijth element of the transpose will be equal to the jith element in the original matrix.
# (2) Reverse each row of the transposed matrix in-place.
#   (2.1) If row-1 is [1, 2, 3], then after reversing it, it should become [3, 2, 1]

def rotate(mat):
    """
    Rotate a matrix 90 degrees clockwise
	
    Argument:
        mat: list of lists
    Return:
        rotated_mat: list of lists
    """
    transposed_mat = []
    for i in range(len(mat[0])):
        row = []
        for j in range(len(mat)):
            row.append(mat[j][i])
        row.reverse()
        transposed_mat.append(row)
    return transposed_mat


print(rotate([[1, 2, 3], [4, 5, 6]]))
#  | 0 1 2
#--|---------
# 0| 1 2 3
# 1| 4 5 6

# transposed matrix
#  |0 1
#--|-------------
# 0|1 4
# 1|2 5
# 2|3 6

# rotated matrix
#  |0 1
#--|-------------
# 0|4 1
# 1|5 2
# 2|6 3