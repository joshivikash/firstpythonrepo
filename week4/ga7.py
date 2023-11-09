o = '7'
n = int(o) % 2003
while (n != 0):
  o += '7'
  n = int(o) % 2003
print(o)
print(len(o))