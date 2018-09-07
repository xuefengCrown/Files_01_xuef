"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    def helper(lists):
        if len(lists) == 1:
            return lists[0]
        minNode, minV, index = lists[0], lists[0].val, 0
        for idx,head in enumerate(lists):
            if head.val < minV:
                minNode = head
                minV = head.val
                index = idx
        if minNode.next:
            lists[index] = minNode.next
        else:
            #lists = lists[:index]+lists[index+1:]
            lists.pop(index)
        minNode.next = None
        minNode.next = helper(lists)
        return minNode
    return helper(lists)
def display(head):
    while head:
        print(head.val, end="-->")
        head = head.next
    print()
    
L1_n1 = ListNode(1)
L1_n4 = ListNode(4)
L1_n5 = ListNode(5)
L1_n1.next = L1_n4
L1_n4.next = L1_n5

L2_n1 = ListNode(1)
L2_n3 = ListNode(3)
L2_n4 = ListNode(4)
L2_n1.next = L2_n3
L2_n3.next = L2_n4

L3_n2 = ListNode(2)
L3_n6 = ListNode(6)
L3_n2.next = L3_n6


display(L1_n1)
display(L2_n1)
display(L3_n2)

lists = [L1_n1, L2_n1, L3_n2]
display(mergeKLists(lists))
