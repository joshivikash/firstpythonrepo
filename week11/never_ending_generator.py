def square(limit):
    while(True):
        yield limit ** 2
        yield limit ** 3

myGenerator = square(5) # type of myGenerator is <class 'generator'>
print(next(myGenerator)) #25
print(next(myGenerator)) #125
print(next(myGenerator)) #25
print(next(myGenerator)) #125
print(next(myGenerator)) #25
print(next(myGenerator)) #125
print(next(myGenerator)) #25
print(next(myGenerator)) #125
print(next(myGenerator)) #25
print(next(myGenerator)) #125
print(next(myGenerator)) #25
print(next(myGenerator)) #125
print(next(myGenerator)) #25
print(next(myGenerator)) #125