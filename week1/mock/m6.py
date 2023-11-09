x = int(input())
i = 5
cfrac = 0
k = x
while i > 0:
  k = x + (1/k) 
  i = i -1
cfrac = k
print(f'{cfrac:.2f}')