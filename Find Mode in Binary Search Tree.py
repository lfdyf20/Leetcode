from collections import defaultdict, Counter
from tryFunc import timer

class Solution(object):
	@timer
	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		def inorder(root):
			if root:
				for nodeVal in inorder(root.left):
					yield nodeVal
				yield root.val
				for nodeVal in inorder(root.right):
					yield nodeVal
		dic = defaultdict(int)
		for nodeVal in inorder(root):
			dic[nodeVal] += 1
		print(dic)
		return [i for i in dic if dic[i]==max(dic.values())]

	@timer
	def online(self, root):

		count = Counter()

		def dfs(node):
			if node:
				count[node.val] += 1
				dfs(node.left)
				dfs(node.right)

		dfs(root)
		max_ct = max(count.itervalues())
		return [k for k, v in count.iteritems() if v == max_ct]



vals = [1,'null',2,2]
from generateBinaryTree import Tree
root = Tree(vals).getTreeRoot()

sl = Solution()
print( sl.findMode( root ) )

print( sl.online(root) )