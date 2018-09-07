# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def llen(lstNode):
        if not lstNode: return 0
        return 1 + llen(lstNode.next)
    
    def add(l, s):
        carry = 0
        lnode, snode, lprev = l, s, l
        while lnode:
            sam = lnode.val + snode.val + carry
            lnode.val = sam%10
            carry = sam//10
            lprev = lnode
            lnode = lnode.next
            if not snode.next:
                snode.next = ListNode(0)
            snode = snode.next

        # 少考虑最高位的进位了
        if carry > 0: lprev.next = ListNode(carry)
        return l
        
    if llen(l1) >= llen(l2): return add(l1, l2)
    return add(l2, l1)
def dis(lNode):
    while lNode:
        print(lNode.val, end='')
        lNode = lNode.next
n9 = ListNode(9)
n9_2 = ListNode(9)
n9.next = n9_2

n1 = ListNode(1)
n5 = ListNode(5)
n5_2 = ListNode(5)
dis(addTwoNumbers(n5, n5_2))




