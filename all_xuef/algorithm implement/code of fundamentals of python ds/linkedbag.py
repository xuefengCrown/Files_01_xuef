"""
File: linkedbag.py
author: xuef
"""
from node import Node
from arraybag import ArrayBag

class LinkedBag(object):
    """ A link-based bag implementation."""
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.items = None
        # When the structure is not empty, self.items refers
        # to the first node in the linked structure.
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
    def add(self, item):
        """Adds item to self."""
        self.items = Node(item, self.items)
        self.size += 1
    def clear(self):
        self.items = None
        self.size = 0
        
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")

        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the one before it, if it exists
        probe = self.items
        trailer = None
        for targetItem in self:
            if targetItem == item: break
            trailer = probe
            probe = probe.next
        # Unhook the node to be deleted, either the first one or the
        # one thereafter
        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self.size -= 1
    # Accessor methods
    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.size
    
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ",".join(map(str, self)) + "}"

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False

        for item in self:
            if not item in other:
                return False
        return True







































        

























    
