
#Consume a generator and send to consumers

def broadcast(source, consumers):
    for item in source:
        for c in consumers:
            c.send(item)

#To create a consumer, define an object with a send() method on it
class Consumer(object):
    def __init__(self, name):
        self.name = name
        
    def send(self,item):
        print(self.name, "got", item)


c1 = Consumer("c1")
c2 = Consumer("c2")
c3 = Consumer("c3")

from examples.follow import follow

lines = follow(open(r"examples\access-log"))
broadcast(lines,[c1,c2,c3])
