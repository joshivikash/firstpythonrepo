def is_magic(mat):
  dim = len(mat)
  first_row_sum = 0
  for i in range(dim):
    first_row_sum += mat[0][i]
  first_col_sum = 0
  for i in range(dim):
    first_col_sum += mat[i][0]
  first_diag_sum = 0
  for i in range(dim):
    first_diag_sum += mat[i][i]
  second_diag_sum = 0
  for i in range(dim):
    second_diag_sum += mat[i][(dim-1)-i]
  print('first_row_sum',first_row_sum)
  print('first_col_sum',first_col_sum)
  print('first_diag_sum',first_diag_sum)
  print('second_diag_sum',second_diag_sum)
  if first_row_sum != first_col_sum or first_diag_sum != second_diag_sum or first_row_sum != first_diag_sum:
    return 'NO'
  for i in range(dim):
    row_sum = 0
    col_sum = 0
    for j in range(dim):
      row_sum += mat[i][j]
      col_sum += mat[j][i]
    if row_sum != first_row_sum or col_sum != first_row_sum:
      return 'NO'
  return 'YES'

print(is_magic([[1,2], [2,1]]))