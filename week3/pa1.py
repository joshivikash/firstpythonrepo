n = int(input())
print('Answers are ....')
for i in range(1, n - 1):
  if (i % 3 == 0 or i % 5 == 0):
    print(i)
