class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList(object):
	"""[summary]
	generate a linked list from input list of vals
	[description]
	"""
	def __init__(self, nodeVals):
		if not nodeVals:
			return None
		self.__head = ListNode(nodeVals[0])
		node = self.__head
		for i in nodeVals[1:]:
			node.next = ListNode(i)
			node = node.next

	def getHead(self):
		"""
		return the head of the linked list
		"""
		return self.__head

	def printLinkedList(self, newHead=None, mode='row'):
		"""
		print the linked list's value, if newHead != None, print that linked list
		"""
		if newHead == None:
			head = self.__head
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

	def reverse(self, head=None):
		"""
		reverse a linked list
		Keyword Arguments:
			head {list node} -- [head of the linked list]
		
		Returns:
			[pre] -- [head of the reversed linked list]
		"""
		if not head:
			head = self.__head
		pre, curr = None, head
		while curr:
			curr.next, pre, curr = pre, curr, curr.next
		self.__head = pre
		return self.__head

	def reverseBetween(self, start, end, head=None):
		"""
		reverse part of linked list
		
		Arguments:
			start {int} -- start with 1
			end {int} -- end point
		
		Keyword Arguments:
			head {list node} -- head of the linked list (default: self.__head)
		
		Returns:
			head -- the head of reversed linked list
		"""
		if not head:
			head = self.__head

		if start >= end:
			return head

		ohead = dummy = ListNode(0)
		whead = wtail = head
		dummy.next = head

		for _ in range( end-start ):
			wtail = wtail.next

		for _ in range( start-1 ):
			ohead, whead, wtail = ohead.next, whead.next, wtail.next

		otail, wtail.next = wtail.next, None
		
		revhead = revtail = self.reverse(whead)
		while revtail and revtail.next:
			revtail = revtail.next
		ohead.next, revtail.next = revhead, otail

		self.__head = dummy.next
		return self.__head

	def removeAt(self, pos, head=None):
		if not head:
			head = self.__head
		if pos == 1:
			self.__head = self.__head.next
			return self.__head

		pre, i = head, 1
		while pre and i<pos-1:
			i += 1
			pre = pre.next
		if pre.next:
			pre.next = pre.next.next
		else:
			pre.next = None
		self.__head = head
		return self.__head 


	def __str__(self):
		curr = self.__head
		output = ""
		while curr:
			output += "{} -> ".format(curr.val)
			curr = curr.next
		return output[:-4]









