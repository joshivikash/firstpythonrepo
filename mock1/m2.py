x = 0
b = 200
while True:
  if x < 10:
    x = int(input('Enter a number: '))
    continue
  elif b < x < b + 2:
    break
