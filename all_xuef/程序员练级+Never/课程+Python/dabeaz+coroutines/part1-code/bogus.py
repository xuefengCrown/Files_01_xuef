# bogus.py
#
# Bogus example of a generator that produces and receives values

def countdown(n):
    print ("Counting down from", n)
    while n >= 0:
        print("before...")
        newvalue = (yield n)
        print("after...")
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1
def test():
    import pdb
    # The holy grail countdown
    c = countdown(5)
    for x in c:
        #pdb.set_trace()
        print(x)
        if x == 5:
            c.send(3)
            
nx=lambda x: print(next(x))
import pdb
c = countdown(5)
pdb.set_trace()
nx(c) # 启动
nx(c) # a
nx(c) # b
nx(c) # c
c.send(4) # d
nx(c) # e
nx(c) # f
