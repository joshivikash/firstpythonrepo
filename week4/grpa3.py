# CODE WITH ALGORITHM
# 1. Accept an integer 'n' as input.
n = int(input())
# 2. Initialize empty lists 'A' and 'B' to store matrices.
A = []
B = []
# 3. Loop 'n' times to accept matrix A:
for i in range(n):
  #     3.1. Initialize an empty list 'row'.
  row = []
  #     3.2. Split the input line by ',' and convert each element to an integer, adding it to 'row'.
  for j in input().split(','):
    row.append(int(j))
#     3.3. Append 'row' to matrix 'A'.
  A.append(row)
# 4. Loop 'n' times to accept matrix B:
for k in range(n):
  #     4.1. Initialize an empty list 'row'.
  row = []
  #     4.2. Split the input line by ',' and convert each element to an integer, adding it to 'row'.
  for l in input().split(','):
    row.append(int(l))
#     4.3. Append 'row' to matrix 'B'.
  B.append(row)
# 5. initialize matrix 'C' as a zero-matrix:
C = []
#     5.1. Loop 'n' times to initialize each element of 'C' to 0.
for p in range(n):
  row = []
  for q in range(n):
    row.append(0)
  C.append(row)
# 6. [Perform matrix product:]
#     6.1. Loop 'n' times to iterate through rows of 'A':
for x in range(n):
  #         6.1.1. Loop 'n' times to iterate through columns of 'B':
  for y in range(n):
    #             6.1.1.1. Initialize a variable 'esum' to 0.
    esum = 0
    #             6.1.1.2. Loop 'n' times to iterate through the elements of 'A' and 'B':
    for z in range(n):
      #                 6.1.1.2.1. Add the product of corresponding elements from 'A' and 'B' to 'esum'.
      esum += A[x][z] * B[z][y]
#             6.1.1.3. Update the corresponding element in 'C' with 'esum'.
    C[x][y] = esum
    #             6.1.1.4. If it's not the last element in the row:
    if y < (n - 1):
      #                 6.1.1.4.1. Print the element followed by a comma.
      print(C[x][y], end=',')
#                 6.1.1.4.2. Else, print the last element in the row without a comma.
    else:
      print(C[x][y])
