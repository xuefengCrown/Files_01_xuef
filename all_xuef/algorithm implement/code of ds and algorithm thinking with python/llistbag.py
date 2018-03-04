# Implements the Bag ADT using a singly linked list.

class Bag:
    # Constructs an empty bag.
    def __init__(self):
        self._head = None
        self._size = 0

    # Return the number of items in the bag.
    def __len__(self):
        return self._size

    # Determines if an item is contained in the bag.
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None

    # Adds a new item to the bag.
    def add(self, item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    # Removes an instance of the item from the bag.
    def remove(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next

        # The item has to be in the bag remove it
        assert curNode is not None, "The item must in the bag."

        # unlink the node and return the item.
        self._size -= 1
        if curNode is self._head: # ???
            self._head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.item

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _BagIterator(self._head) #???

# Defines a private storage class for creating list nodes.
class _BagListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# Defines a linked list iterator for the Bag ADT
class _BagIterator:
    def __init__(self, listHead):
        self._curNode = listHead
    def __iter__(self):
        return self
    def next (self):
        if self._curNode is Node:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item

ballbag = Bag()
ballbag.add("red ball")
ballbag.add("blue ball")
ballbag.add("black ball")
ballbag.remove("black ball")

print(ballbag._head.item)





















        





















































        
