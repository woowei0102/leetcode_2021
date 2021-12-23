# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
           return None
        pos = head
        while pos and pos.next:
            if pos.val == pos.next.val:
                pos.next = pos.next.next
            else:
                pos = pos.next
        return head
