


def num():
    i = 1
    while 1:
        yield i
        i += 1
g = num()
##while 1:
##    print(next(g))

for i in g:
    print(i)
