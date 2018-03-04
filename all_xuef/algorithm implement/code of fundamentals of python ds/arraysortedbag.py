"""
File: arraysortedbag.py
author: xuef
"""
from arraybag import ArrayBag

class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""
    # Constructor
    def __init__(self, sourceCollection = None):
        ArrayBag.__init__(self, sourceCollection)
        
    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right)//2
            if self.items[midPoint] == item:
                return True
            elif self.items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item >= self.items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Resize the array if it is full here
            # Search for first item >= new item
            targetIndex = 0
            while item > self.items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self.items[i] = self.items[i - 1]
            # Insert item and update size
            self.items[targetIndex] = item
            self.size += 1




































            
