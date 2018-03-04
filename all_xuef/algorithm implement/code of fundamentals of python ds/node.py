
class Node(object):
    """Represents a singly linked node."""
    def __init__(self, data, nxt = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = nxt
        
