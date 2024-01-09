a = [10,20,30,40,50,60,70]
b = [1,2,3,4,5]
print(list(map(lambda n,m: n * m, a,b))) # [10, 40, 90, 160, 250]
print(list(map(lambda n,m: n * m, b,a))) # [10, 40, 90, 160, 250]