def get_column(mat, col):
    '''Will return the column as list located at index col'''
    l = []
    for i in range(len(mat)):
        l.append(mat[i][col])
    return l

def get_row(mat,row):
    '''It gets a list of row located at index row'''
    l = []
    for i in range(len(mat[0])):
        l.append(mat[row][i])
    return l

print(get_column([[1, 2], [3, 4]], 0))
print(get_row([[1, 2], [3, 4]], 1))
print(get_row([[1, 2], [3, 4], [5, 6]], 1))
print(get_column([[1, 2], [3, 4], [5, 6], [7, 8]], 1))