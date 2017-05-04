from collections import deque
class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		depth = 1
		stack = deque([(root, depth)])
		while stack:
			node, depth = stack.popleft()
			if not node.left and not node.right:
				return depth
			if node.left:
				stack.append( (node.left, depth+1) )
			if node.right:
				stack.append( (node.right, depth+1) )


	def online(self, root):
		if not root: return 0
		d = map(self.minDepth, (root.left, root.right))
		return 1 + (min(d) or max(d))


vals = [1,2,3,4,5,'null',5,8,'null',7,8,'null','null','null','null',9]
vals = [3,9,20,'null','null',15,7]

from generateBinaryTree import Tree
root = Tree(vals).getTreeRoot()

sl = Solution()
print( sl.minDepth( root ) )