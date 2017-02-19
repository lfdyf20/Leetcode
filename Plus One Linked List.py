# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        carry = self.backtrack(head)
        if head.val == 0 and carry == 1:
            newHead = ListNode( 1 )
            newHead.next = head
            return newHead
        return head
        
    def backtrack(self, head):
        if not head.next:
            val = head.val + 1
            if val >= 10:
                head.val = val%10
                return 1
            head.val = val
            return 0
        
        carry = self.backtrack(head.next)
        if carry:
            val = head.val + 1
            if val >= 10:
                head.val = val%10
                return 1
        head.val += carry
        return 0