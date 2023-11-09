def get_column(mat, col):
  rows = len(mat)
  cols = []
  for i in range(rows):
    cols.append(mat[i][col])
  return cols

def get_row(mat, row):
    return mat[row]