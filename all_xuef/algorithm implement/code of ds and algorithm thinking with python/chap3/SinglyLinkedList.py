

# node of a singly linked list
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, nxt):
        self.next = nxt

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

class LinkedList:
    def __init__(self, hNode):
        self.head = hNode
    def listLen(self) :
        current = self.head
        cnt = 0
        while current != None:
            cnt += 1
            current = current.getNext()
        return cnt

    """
    Insertion  into  a  singly-linked list has three cases:
        Inserting  a new node  before  the  head  (at the beginning)
        Inserting  a new node  after  the  tail  (at  the  end  of  the list)
        Inserting  a new node  at the middle of the  list  (random location)
    """
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.setNext(node2)
node2.setNext(node3)

linkedList = LinkedList(head)

length = linkedList.listLen()
print(length)
















