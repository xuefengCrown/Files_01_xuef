# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head_l1 = l1.val
        head_l2 = l2.val
        if head_l1 <= head_l2:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        if head_l1 > head_l2:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
def iterLst(lst):
    while lst is not None:
        print(lst.val, end="->")
        lst = lst.next
# lst1: 1->2->4
# lst2: 1->3->4
l1_node4 = ListNode(4)
l1_node2 = ListNode(2, l1_node4)
l1_node1 = ListNode(1, l1_node2)

l2_node4 = ListNode(4)
l2_node3 = ListNode(3, l2_node4)
l2_node1 = ListNode(1, l2_node3)

# iterLst(l1_node1)

sol = Solution()
iterLst(sol.mergeTwoLists(l1_node1, l2_node1))
