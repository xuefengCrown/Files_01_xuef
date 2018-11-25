

def fib():
    a,b = 1,1
    while True:
        yield a
        a,b = b,a+b

for i in fib():
    print(i)
