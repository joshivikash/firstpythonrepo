def transpose(mat):
  """
  compute the transpose of the matrix

  Argument:
      mat: list of lists
  Return:
      mat_trans: list of lists
  """
  tranposed_mat = []
  for i in range(len(mat[0])):
    row = []
    for j in range(len(mat)):
      row.append(mat[j][i])
    tranposed_mat.append(row)
  return tranposed_mat


print(transpose([[1, 2, 3], [4, 5, 6]]))
