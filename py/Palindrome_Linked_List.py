# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):

        ## method 1
        # if head is None:
        #     return True
        # p1 = p2 = head
        # p3, pre = p1.next, p1
        # while p2.next and p2.next.next:
        #     p2 = p2.next.next
        #     pre = p1
        #     p1 = p3
        #     p3 = p3.next
        #     p1.next = pre
        # if p2.next is None:
        #     p1 = p1.next

        # while p3:
        #     if p1.val != p3.val:
        #         return False
        #     p1 = p1.next
        #     p3 = p3.next
            
        # return True

        ## method 2
        # a = b = ""

        # while(head):
        #     a = a + str(head.val)
        #     b = str(head.val) + b
        #     head = head.next
        
        # return a == b

        ## method 3
        def reverseList(h):
            if h is None or h.next is None:
                return h
            p = reverseList(h.next)
            h.next.next = h
            h.next = None
            return p

        
        if head is None or head.next is None:
            return True

        lt = l = ListNode(-1)
        t = head
        c = 0
        while t:
            lt.next = ListNode(t.val)
            t = t.next
            lt = lt.next
            
        r = reverseList(head)
        

        while r:
            if l.next.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
        