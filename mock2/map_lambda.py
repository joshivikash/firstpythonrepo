n = 123456
str_n = str(n)
L1 = list(map(int,str_n))
print(L1)
L2 = list(map(lambda x: x ** len(str_n), L1))
print(L2)
s = 'vikash'
print(s[-1:-7:-1])
