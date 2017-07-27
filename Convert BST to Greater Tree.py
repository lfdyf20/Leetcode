from Tree import BinaryTree
class Solution(object):
	def convertBST(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""

		def treeSum(root, preSum):
			if root:
				rightSum = treeSum(root.right, preSum)
				preRootVal = root.val
				root.val += rightSum + preSum
				leftSum = treeSum(root.left, root.val)
				return leftSum + preRootVal + rightSum
			return 0

		treeSum(root, 0)
		return root


			


t = [2,0,3,-4,1]
tree = BinaryTree(t)
# print(tree)

sl = Solution()
root = sl.convertBST( tree.getTreeRoot() )

tree.drawTree(root)