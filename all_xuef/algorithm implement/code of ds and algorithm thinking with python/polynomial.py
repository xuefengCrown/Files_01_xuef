
# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

# Implementation of the Polynomial ADT using a sorted linked list.
class Polynomial:
    # Create a new polynomial object.
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead
    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree
    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree>=degree:
            curNode = curNode.next

        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.coefficient


























            





















    
        
