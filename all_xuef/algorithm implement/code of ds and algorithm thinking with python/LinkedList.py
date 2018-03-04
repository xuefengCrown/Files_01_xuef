

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

def unorderedSearch(head, target):
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode= curNode.next
    return curNode is not None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

traversal(a)
