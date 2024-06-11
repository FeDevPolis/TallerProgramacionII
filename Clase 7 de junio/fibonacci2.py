def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(10):
    print(x)