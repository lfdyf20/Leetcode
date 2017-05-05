class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		if not head:
			return
		newHead = head
		while newHead.val == val and newHead.next:
			newHead = newHead.next
		if not newHead.next:
			if newHead.val == val:
				return

		node = newHead
		while node.next:
			if node.next.val == val:
				node.next = node.next.next
			else:
				node = node.next
		return newHead
		



from generateLinkedList import LinkedList

vals = [6,1,3,6,6,4,6,7,6,6]
vals = [1]
ls = LinkedList(vals)
head, val = ls.getHead(), 1

sl = Solution()
newHead =  sl.removeElements( head, val )
ls.printLinkedList(newHead)
