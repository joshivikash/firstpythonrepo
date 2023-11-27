import time
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

limit = 1000000000 
sorted_list = []
print('populating the list...')
for i in range(limit):
    sorted_list.append(i)
print('inserting...')
a = time.time()
insert(sorted_list,limit)
b = time.time()
print('time taken for inserting the element {}'.format(b - a))