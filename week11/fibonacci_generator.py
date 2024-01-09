def fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a + b

print(f'type of fib(3) is {type(fib(3))}')
for i in fib(5):
    print(i)