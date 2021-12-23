# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # add a extra head for removing head
        pre = ListNode(-1)
        pre.next = head
        last, pos = pre, head
        while pos:
            if pos.val == val:
                last.next = pos.next
            else:
               last = pos
            pos = pos.next
        return pre.next
