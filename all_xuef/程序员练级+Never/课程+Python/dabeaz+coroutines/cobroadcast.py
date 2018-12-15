# cobroadcast.py
#
# An example of broadcasting a data stream onto multiple coroutine targets.

from coroutine import coroutine

# A data source.  This is not a coroutine, but it sends
# data into one (target)

import time
def follow(thefile, target):
    #thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         target.send(line)

# A filter.
@coroutine
def grep(pattern,target):
    while True:
        line = (yield)           # Receive a line
        if pattern in line:
            target.send(line)    # Send to next stage

# A sink.  A coroutine that receives data
@coroutine
def printer():
    while True:
         line = (yield)
         print (line)

# Broadcast a stream onto multiple targets
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
##This takes a sequence of coroutines (targets)
##and sends received items to all of them.

# Example use
if __name__ == '__main__':
    f = open("access-log")
    follow(f,
       broadcast([grep('python',printer()),
                  grep('ply',printer()),
                  grep('swig',printer())])
           )

"""
Coroutines provide more powerful data routing
possibilities than simple iterators
•
If you built a collection of simple data processing
components, you can glue them together into
complex arrangements of pipes, branches,
merging, etc.
•
Although there are some limitations (later)
"""
