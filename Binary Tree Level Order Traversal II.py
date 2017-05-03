class Solution(object):
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		res, queue =[], [root]
		while queue:
			res.append( [node.val for node in queue if node] )
			queue = [ child for node in queue if node for child in [node.left, node.right] ]
		print(queue)
		print(res)
		return res[-2::-1]







vals = [3,9,20,'null','null',15,7]
vals = [1,2,3,4,'null', 'null', 5]
from generateBinaryTree import Tree
tree = Tree(vals)
root = tree.getTreeRoot()


sl = Solution()
print( sl.levelOrderBottom( root ) )



tree.drawtree()
def inorder(root):
	if root:
		for node in inorder(root.left):
			yield node
		yield root.val
		for node in inorder(root.right):
			yield node

for nodeVal in inorder(root):
	print(nodeVal)