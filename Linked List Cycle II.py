class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
        	slow = slow.next
        	fast = fast.next.next
        	if slow == fast:
        		break
        else:
        	return None
        while head != slow:
        	slow = slow.next
        	head = head.next
        return head