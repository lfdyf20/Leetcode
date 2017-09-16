class Solution(object):
	def largestBSTSubtree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		def dfs(node):
			if not node:
				return 0, 0, float('inf'), float('-inf')
			N1, n1, min1, max1 = dfs(node.left)
			N2, n2, min2, max2 = dfs(node.right)
			n = n1 + n2 + 1 if max1 < node.val < min2 else float('-inf')
			return max(N1, N2, n), n, min(min1, node.val), max(max2, node.val) 

		return dfs(root)[0]

	# def largestBSTSubtree(self, root):
	# 	def dfs(root):
	# 		if not root:
	# 			return 0, 0, float('inf'), float('-inf')
	# 		N1, n1, min1, max1 = dfs(root.left)
	# 		N2, n2, min2, max2 = dfs(root.right)
	# 		n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
	# 		return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
	# 	return dfs(root)[0]



vals = '[10,5,15,1,8,null,7]'
from Tree import BinaryTree
t = BinaryTree(vals)
root = t.getRoot()

sl = Solution()
print( sl.largestBSTSubtree( root ) )