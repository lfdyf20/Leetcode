class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, curr = head, head.next
        while curr:
            if pre.val != curr.val:
                pre.next = curr
                pre = pre.next
            curr = curr.next
        pre.next = None
        return head