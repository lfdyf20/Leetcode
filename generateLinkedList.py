class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self, nodeVals):
		if not nodeVals:
			return None
		self.head = ListNode(nodeVals[0])
		node = self.head
		for i in nodeVals[1:]:
			node.next = ListNode(i)
			node = node.next

	def getHead(self):
		return self.head

	def printLinkedList(self, newHead=None, mode='row'):
		if newHead == None:
			head = self.head
		else:
			head = newHead
		if mode == 'row':
			res = ''
			while head and head.next:
				res += str(head.val) + '->'
				head = head.next
			res += str(head.val)
			print(res)
		else:
			while head:
				print(head.val)
				head = head.next

