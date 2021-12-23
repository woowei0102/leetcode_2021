# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def addTwoNumbers(self, l1, l2):
        carry = 0
        # dummy head
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val // 10
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next

    def printList(self, l):
        result = 0
        while l:
            result = result*10 + l.val
            l = l.next
        return result
    
    def buildList(self, nums):
        # nums = list(reversed(nums))
        l = head = ListNode(0)
        for i in range(len(nums)):
            l.next = ListNode(nums[i])
            l = l.next
        return head.next

if __name__ == '__main__':
    s = Solution()
    s1 = [9, 9, 9, 9, 9, 9, 9]
    s2 = [9, 9, 9, 9]
    # s1 = [2, 4, 3]
    # s2 = [5, 6, 4]
    list1 = s.buildList(s1)
    list2 = s.buildList(s2)

    ans = s.addTwoNumbers(list1, list2)
    
    print(s.printList(ans))
