from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class BinaryTree(object):
	def __init__(self, vals):
		if not vals:
			self.root = None
		# nodes = [None if val == 'null' else TreeNode(int(val))
				 # for val in string.strip('[]{}').split(',')]
		nodes = [None if val == 'null' else TreeNode(int(val))
				 for val in vals]
		kids = nodes[::-1]
		self.root = kids.pop()
		for node in nodes:
			if node:
				if kids: node.left  = kids.pop()
				if kids: node.right = kids.pop()

	def __str__(self):
		self.drawTree()
		return self.preorderTravesal()


	def getTreeRoot(self):
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