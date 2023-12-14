a = int(input())
b = int(input())

for i in range(a):
    if i == 0 or i == (a - 1):
        print('o' * b, sep='')
    else:
        print('o',' ' * (b - 2),'o', sep='')