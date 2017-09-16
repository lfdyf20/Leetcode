# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

from DecoratorHelper import drawBinaryTree
class Solution(object):
	@drawBinaryTree
	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		def build(inorder, postorder):
			if not postorder or not inorder:
				return None
			rootVal = postorder.pop()
			index = inorder.index(rootVal)
			root = TreeNode(rootVal)
			root.right = build(inorder[index+1:], postorder)
			root.left = build(inorder[:index], postorder)
			return root

		return build(inorder, postorder)





inorder, postorder = [4,2,6,5,1,7,3], [4,6,5,2,7,3,1]
# inorder, postorder = [], []


sl = Solution()
root = sl.buildTree( inorder, postorder )

