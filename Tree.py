from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def __str__(self) -> str:
		return str(self.val)

class AVLTreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.height = 0


class BinaryTree(object):
	"""Binary Tree
	
	This is a binary tree generator
	"""
	
	def __init__(self, vals):
		"""
		Generate a Binary Tree from a string
		Arguments:
			vals {string} -- val for each node in the form like '[1,2,3]'
		"""
		if not vals:
			self.root = None
		nodes = [None if val == 'null' else TreeNode(int(val))
				 for val in vals.strip('[]{}').split(',')]
		# nodes = [None if val == 'null' else TreeNode(int(val))
		# 		 for val in vals]
		kids = nodes[::-1]
		self.root = kids.pop()
		for node in nodes:
			if node:
				if kids: node.left  = kids.pop()
				if kids: node.right = kids.pop()

	def __str__(self):
		self.drawTree()
		self.preorderTravesal()
		return "".join(str(i) for i in self.preorderTravesal())


	def getRoot(self):
		"""
		get tree root
		"""
		return self.root

	def inorderTravesal(self):
		root = self.root
		res, stack = [], []
		while True:
			while root:
				stack.append( root )
				root = root.left
			if not stack:
				return res
			node = stack.pop()
			res.append( node.val )
			root = node.right
		return res

	def preorderTravesal(self):
		root = self.root
		res, stack = [], [root]
		while stack:
			node = stack.pop()
			if node:
				res.append( node.val )
				stack += [ node.right, node.left ]
		return res

	def postorderTravesal(self):
		root = self.root
		res, stack = [], [root]
		while stack:
			node = stack.pop()
			if node:
				res.append( node.val )
				stack += [ node.left, node.right ]
		return res[::-1]

	def drawTree(self, root=None):
		if root == None:
			root = self.root
		def height(root):
			return 1 + max(height(root.left), height(root.right)) if root else -1
		
		def jumpto(x, y):
			t.penup()
			t.goto(x, y)
			t.pendown()
		
		def draw(node, x, y, dx):
			if node:
				t.goto(x, y)
				jumpto(x, y-20)
				t.write(node.val, align='center', font=('Arial', 12, 'normal'))
				draw(node.left, x-dx, y-60, dx/2)
				jumpto(x, y-20)
				draw(node.right, x+dx, y-60, dx/2)
		
		import turtle
		t = turtle.Turtle()
		t.speed(0); turtle.delay(0)
		h = height(root)
		jumpto(0, 30*h)
		draw(root, 0, 30*h, 40*h)
		t.hideturtle()
		turtle.mainloop()





class AVL(object):

	def __init__(self):
		self.root = None


	def insert(self, val, node):
		self.root = self.insertNode(val, self.root)


	def insertNode(self, val, node):
		if not node:
			return AVLTreeNode(val)
		
		if val < node.val:
			node.left = self.insertNode(val, node.left)
		else:
			node.right = self.insertNode(val, node.right)
		
		node.height = max( self.calcHeight(node.left), self.calcHeight(node.right) ) + 1
		return self.settleViolation(val, node) 


	def settleViolation(self, val, node):
		balance = self.calcBalance(node)

		# inserted newNode is left child of left child of node
		if balance > 1 and val < node.left.val:
			return self.rotateRight(node)

		# inserted newNode is right child of right child of node
		if balance < -1 and val > node.right.val:
			return self.rotateLeft(node)
		
		# # inserted newNode is right child of left child of node 
		if balance > 1 and val > node.left.val:
			node.left = self.rotateLeft(node.left)
			return self.rotateRight(node)

		# # inserted newNode is left child of right child of node 
		if balance < -1 and val < node.right.val:
		 	node.right = self.rotateRight(node.right)
		 	return self.rotateLeft(node)	


	def calcHeight(self, node):

		if not node:
			return -1
		return node.height


	def calcBalance(self, node):
		"""
		if return value > 1: means this is a left heavy tree. rotate right
		if return value < 1: means this is a right heavy tree. rotate left
		"""
		if not node:
			return 0

		return self.calcHeight(node.left) - self.calcHeight(node.right)


	def rotateRight(self, node):
		print("rotate to right on node ", node.val)

		newRoot = node.left
		nodeToShift = newRoot.right

		node.left = nodeToShift
		newRoot.right = node

		node.height = max( self.calcHeight(node.left), self.calcHeight(node.right) ) + 1
		newRoot.height = max( self.calcHeight(newRoot.left), self.calcHeight(newRoot.right) ) + 1

		return newRoot


	def rotateLeft(self, node):
		print("rotate to left on node ", node.val)

		newRoot = node.right
		nodeToShift = newRoot.left

		node.right = nodeToShift
		newRoot.left = node

		node.height = max( self.calcHeight(node.left), self.calcHeight(node.right) ) + 1
		newRoot.height = max( self.calcHeight(newRoot.left), self.calcHeight(newRoot.right) ) + 1

		return newRoot




