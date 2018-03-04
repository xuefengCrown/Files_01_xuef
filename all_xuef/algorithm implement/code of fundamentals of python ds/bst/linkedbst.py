"""
File: linkedbst.py
author: xuef
"""
from bstnode import BSTNode

class LinkedBST():
    def __init__(self, sourceCollection = None):
        self.root = None
        self.size = 0

    def find(self, item):
        # helper func
        def f(node):
            if node is None: return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return f(node.left)
            else:
                return f(node.right)
        return f(self.root)

    def inorder(self):
        lyst = list()
        def f(node):
            if node != None:
                f(node.left)
                lyst.append(node.data)
                f(node.right)
        f(self.root)
        return iter(lyst)

    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level+1)
                s += "|" * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self.root, 0)

    def add(self, item):
        newNode = BSTNode(item)
        def add_helper(node):
            if self.root is None:
                self.root = newNode
                return
            if item<node.data:
                if node.left is None:
                    node.left = newNode
                else:
                    add_helper(node.left)
            else:
                if node.right is None:
                    node.right = newNode
                else:
                    add_helper(node.right)

        add_helper(self.root)
        self.size += 1  

    def remove(self, item):
        pass # ???????????
    
bst = LinkedBST()
bst.add("D")
bst.add("B")
bst.add("A")
bst.add("C")
bst.add("F")
bst.add("E")
bst.add("G")

for ele in bst.inorder():
    print(ele)

print(bst.size)























        
