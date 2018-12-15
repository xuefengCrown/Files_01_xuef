

def gen():
    n = 1
    while True:
        try:
            yield n
            n += 1
        except GeneratorExit:
            # shut down
            print("gen exit")
        

g = gen()
print(next(g))
print(next(g))
print(next(g))
g.close()

