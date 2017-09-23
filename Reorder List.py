class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
        	return

        slow = fast = head

        while fast and fast.next:
        	slow = slow.next
        	fast = fast.next.next

        pre, node = None, slow
        while node:
        	node.next, pre, node= pre, node, node.next

        first, second = head, pre
        while second.next:
        	first.next, first = second, first.next
        	second.next, second = first, second.next

       	return 



vals = [1,2,3,4]

from LinkedList import LinkedList
l = LinkedList(vals)
head = l.getHead()
print(l)

sl = Solution()
print( sl.reorderList( head ) )
