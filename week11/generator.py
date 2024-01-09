def myList(limit):
    x = 0
    while x < limit:
        yield x
        x += 1

print(f'type of myList(5) is {type(myList(5))}') # type of myList(5) is <class 'generator'>
print(f'type of myList is {type(myList)}') # type of myList is <class 'function'>

for i in myList(5):
    print(i)