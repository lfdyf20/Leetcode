# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from DecoratorHelper import drawBinaryTree
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def addLeft(node):
        	if node:
        		if not node.left and not node.right:
        			return
        		left.append(node.val)
        		if node.left:
        			addLeft(node.left)
        		elif node.right:
        			addLeft(node.right)
        		else:
        			return

        def addRight(node):
        	if node:
        		if not node.left and not node.right:
        			return
        		right.append(node.val)
        		if node.right:
        			addRight(node.right)
        		elif node.left:
        			addRight(node.left)
        		else:
        			return

        def addLeaves(node):
        	if node:
        		if not node.left and not node.right:
        			leaves.append(node.val)
        			return
        		addLeaves(node.left)
        		addLeaves(node.right)


        left, leaves, right = [], [], []
        if not root.left:
        	left.append(root.val)
        else:
        	addLeft(root)
        if root.left or root.right:
        	addLeaves(root)
        addRight(root.right)

        print(left, leaves, right)

        return left + leaves + right[::-1]
        


vals = '[1,null,2,3,4]'
# vals = '[1,2,3,4,5,6,null,null,null,7,8,9,10]'
vals = '[1]'

from Tree import BinaryTree

t = BinaryTree(vals)
root = t.getRoot()

sl = Solution()
print( sl.boundaryOfBinaryTree( root ) )