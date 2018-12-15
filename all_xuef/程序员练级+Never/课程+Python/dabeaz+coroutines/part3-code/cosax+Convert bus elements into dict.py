# cosax.py
#
# An example showing how to push SAX events into a coroutine target

import xml.sax

class EventHandler(xml.sax.ContentHandler):
    def __init__(self,target):
        self.target = target # 注入协同程序(data processing)
    def startElement(self,name,attrs):
        self.target.send(('start',(name,attrs._attrs)))
    def characters(self,text):
        self.target.send(('text',text))
    def endElement(self,name):
        self.target.send(('end',name))
"""
Event Processing
    To do anything interesting, you have to process the event stream
    Example: Convert bus elements into dictionaries (XML sucks, dictionaries rock)
"""
# example use
if __name__ == '__main__':
    from coroutine import coroutine

    @coroutine
    def printer():
        while True:
            data = (yield) # receive data
            print (data)

    #Filtering Elements
    #Let's filter on dictionary fields
    #####################
    #filter_on_field("route","22",target)
    # filter_on_field("direction","North Bound",target)
    #####################
    @coroutine
    def filter_on_field(fieldname,value,target):
        while True:
            d = (yield)
            if d.get(fieldname) == value:
                target.send(d)


    #Processing Elements
    #Where's my bus?
    """
    This receives dictionaries and prints a table
    22,1485,"North Bound",41.880481123924255,-87.62948191165924
    22,1629,"North Bound",42.01851969751819,-87.6730209876751
    ..
    """
    @coroutine
    def bus_locations():
        while True:
            bus = (yield)
        print ("%(route)s,%(id)s,\"%(direction)s\","\
                "%(latitude)s,%(longitude)s" % bus)
    

    @coroutine
    def xml2dict(target):
        # 避免了数据的结构嵌套
        # 省去了pack数据，然后再unpack数据的过程?!!
        while True:
            event, value = (yield) # receive sax event
            # Look for the start of a <bus> element
            if event == "start" and value[0] == "bus":
                busdict = { }
                fragments = []
                while True:
                    event, value = (yield)
                    if event == "start": # new tag
                        fragments = []
                    elif event == "text":
                        fragments.append(value)
                    else:
                        if value == "bus":
                            target.send(busdict)
                            break
                        else:
                            busdict[value] = "".join(fragments)
                        

    #Hooking it Together
    ##Find all locations of the North Bound #22 bus (the slowest moving object in the universe)
    """
    xml.sax.parse("allroutes.xml",
                    EventHandler(
                        buses_to_dicts(
                                filter_on_field("route","22",
                                        filter_on_field("direction","North Bound",
                                                        bus_locations())))
                    ))
    """

    xml.sax.parse(r"..\coroutines\allroutes.xml",
                  EventHandler(xml2dict(printer())))


    """
    One interesting thing about coroutines is that you can push the initial data source as
    low-level as you want to make it without rewriting all of the processing stages
    """
