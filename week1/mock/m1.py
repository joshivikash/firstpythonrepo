'''
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1
'''
n = int(input())
for i in range(1, n):
  j = 1
  while j <= i + 1:
    print(j, end = " ")
    j += 1
  j = j - 2
  for k in range(j, 0, -1):
    print(k, end = " ")
  print()