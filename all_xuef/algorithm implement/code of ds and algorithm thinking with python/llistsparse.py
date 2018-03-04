
# Implementation of the Sparse Matrix ADT using an array of linked lists.
from array import Array

class SparseMatrix:
    # Creates a sparse matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self._listOfRows = Array(numRows)
    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, value):
        predNode = None
        curNode = self._listOfRows[row]



























        
# Storage class for creating matrix element nodes.
class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None
