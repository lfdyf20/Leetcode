# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		if not head:
			return None
		if not head.next:
			return TreeNode(head.val)

		l = r = head
		pre = ListNode(0)
		pre.next = head

		while r and r.next and r.next.next:
			pre, l, r = pre.next, l.next, r.next.next
		if r.next:
			pre, l = pre.next, l.next

		pre.next, root = None, l
		left, right = head, root.next
		troot = TreeNode(root.val)
		troot.left = self.sortedListToBST(left)
		troot.right = self.sortedListToBST(right)

		return troot






vals = [1,2,3]

from LinkedList import LinkedList

l = LinkedList(vals)

head = l.getHead()

sl = Solution()
root = sl.sortedListToBST( head )


# Draw a Binary Tree
def drawTree(root):
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

drawTree(root)