"""
File: arrays.py
author: xuef

an Array is like a list, but the client can use only
[], len, iter, and str.

to instantiate, use
<variable> = Array(<capacity>, <optional fill value>)
the fill value is None by default.
"""
class Array(object):
    """Represent an array"""
    def __init__(self, capacity, fillValue=None):
        """capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """->the capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__ (self, index):
        """Subscript operator for access at index."""
        return self.items[index]
    def __setitem__ (self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem
















