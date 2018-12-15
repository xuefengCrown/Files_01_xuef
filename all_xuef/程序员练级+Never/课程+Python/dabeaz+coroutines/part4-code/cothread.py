# cothread.py
#
# A thread object that runs a coroutine inside it.  Messages get sent
# via a Queue object

from threading import Thread
from Queue import Queue
from coroutine import *

@coroutine
def threaded(target):
    messages = Queue() #A message queue
    ##########################
    #A thread. Loop forever, pulling items out of the message queue
    #and sending them to the target
    def run_target():
        while True:
            item = messages.get()
            if item is GeneratorExit: #Handle close() so that the thread shuts down correctly
                target.close()
                return
            else:
                target.send(item)
    Thread(target=run_target).start()
    ##########################

    #Receive items and pass them into the thread (via the queue)
    try:
        while True:
            item = (yield)
            messages.put(item)
    except GeneratorExit:#Handle close() so that the thread shuts down correctly
        messages.put(GeneratorExit)

# Example use

if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler
    from buses import *

    xml.sax.parse("allroutes.xml", EventHandler(
                    buses_to_dicts(
                    threaded(
                         filter_on_field("route","22",
                         filter_on_field("direction","North Bound",
                         bus_locations()))
                    ))))
                 
"""
#Main Program
  xml.sax.parse
        |
  EventHandler
        |            Thread
  buses_to_dicts------->filter_on_field
                                |
                        filter_on_field
                                |
                        bus_locations
"""
