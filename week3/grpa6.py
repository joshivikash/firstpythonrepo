n = int(input())
for i in range(n):
    for j in range(i + 1):
      if(j < i):
        print(j+1, end = ",")
      else:
        print(j+1, end = "")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
      if(j < i - 1):
        print(j+1, end = ",")
      else:
        print(j+1, end = "")
    print()