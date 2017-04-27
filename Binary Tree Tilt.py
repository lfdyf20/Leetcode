# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	tilt = 0
	def findTilt(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.dfs(root)
		return self.tilt


	def dfs(self, root):
		if root:
			left = self.dfs(root.left)
			right = self.dfs(root.right)
			self.tilt += abs(left-right)
			return left + right + root.val
		return 0