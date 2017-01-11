class linkedList(object):
	"""docstring for linkedList"""
	def __init__(self, nodesList):
		self.head = nodesList[0]
		self.tail = nodesList[0]
		for i in nodesList[1:]:
			self.tail.next = nodesList[i]
			self.tail = self.tail.next

	def addNode(self, node):
		self.tail.next = node
		self.tail = self.tail.next

	def removeNode(self,node):
		curr = self.head
		while curr.next.next:
			curr = curr.next
		curr.next = None
		


		

class linkedNode(object):
	"""docstring for linkedNode"""
	def __init__(self, x):
		self.val = x
		self.next = None
		