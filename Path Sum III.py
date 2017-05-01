# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	res = 0

	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		""" 
		def dfs(root, vals, sum):
			if root:
				nodeVals = []
				for val in vals + [0]:
					tempSum = val + root.val
					if tempSum == sum:
						self.res += 1
					nodeVals.append( tempSum )
				dfs(root.left, nodeVals, sum)
				dfs(root.right, nodeVals, sum)

		dfs(root, [], sum)
		return self.res






vals = [10,5,-3,3,2,'null',11,3,-2,'null',1]
from generateBinaryTree import Tree
tree = Tree( vals )
root = tree.getTreeRoot()

sl = Solution()
print( sl.pathSum(root, 8) )

print( tree.inorderTravesal() )
print( tree.preorderTravesal() )
print( tree.postorderTravesal() )

tree.drawtree()