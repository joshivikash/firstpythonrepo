def generate():
    yield 100

for i in generate():
    print(i)