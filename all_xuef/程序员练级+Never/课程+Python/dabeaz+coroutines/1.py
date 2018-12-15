#协同程序

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.__next__()
        return cr
    return start


def grep(pattern):
    print ("Looking for %s" % pattern)
    while True:
        print("--------")
        line = (yield)
        print("++++++++")
        if pattern in line:
            print (line)


#The pipeline must have an end-point (sink)
#Collects all data sent to it and processes it
@coroutine
def sink():
    try:
        while True:
            item = (yield) # Receive an item
        
    except GeneratorExit: # Handle .close()
        pass
    

            
def test_grep():
    import pdb
    pdb.set_trace()
    g = grep("python")
    next(g) # Prime it (explained shortly)
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")


################################################################
import time
def follow(thefile, target):
    #thefile.seek(-300,2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        target.send(line)

@coroutine
def printer():
    while True:
        line = (yield)
        print (line)

#Hooking it together
def m2():
    f = open("access-log")
    follow(f, printer())
"""
         send()
follow()-------> printer()

Critical point : follow() is driving the entire
computation by reading lines and pushing them
into the printer() coroutine
"""
#################################################################

#Pipeline Filters
##Intermediate stages both receive and send
##Typically perform some kind of data transformation, filtering, routing, etc.
@coroutine
def filter(target):
    while True:
        item = (yield) # Receive an item
        # Transform/filter item
        # ...
        # Send it along to the next stage
        target.send(item)


###################
#A Filter Example
###################
@coroutine
def grep2(pattern,target):
    while True:
        line = (yield) # Receive a line
        if pattern in line:
            target.send(line) # Send to next stage
def t2():
    f = open("access-log")
    follow(f,
            grep2('python', printer())
           )        

"""
Generators pull data through
the pipe with iteration. Coroutines push data
into the pipeline with send().
"""
