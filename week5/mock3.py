def insert(L, x):
  new_list = []
  inserted = False
  for i in range(len(L)):
    if not inserted and L[i] > x:
      new_list.append(x)
      inserted = True
    new_list.append(L[i])
  if len(new_list) == len(L):
      new_list.append(x)
  return new_list