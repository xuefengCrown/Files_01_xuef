"""
File: arraybag.py
Author: xuef
"""
from arrays import Array

class ArrayBag(object):
    """An array-based bag implementation."""

    # class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
    def add(self, item):
        self.items[len(self)] = item
        self.size += 1
        if self.size * 2 > ArrayBag.DEFAULT_CAPACITY:
            ArrayBag.DEFAULT_CAPACITY *= 2
            newArray = Array(ArrayBag.DEFAULT_CAPACITY)
            for i in range(self.size):
                newArray[i] = self.items[i]
            self.items = newArray
            

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

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

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")

        # Search for index of target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i+1]
        # Decrement logical size
        self.size -= 1

def test():
    arr = ArrayBag([i*i for i in range(1,20)])
    print(arr)
    print(ArrayBag.DEFAULT_CAPACITY)

test()















        

















            














        


















    
        









    







        








        










    
