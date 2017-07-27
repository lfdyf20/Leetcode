class Solution(object):
	def isSubtree(self, s, t):
		"""
		:type s: TreeNode
		:type t: TreeNode
		:rtype: bool
		"""
		def dfs(s, t, pre = False):
			if not s and not t:
				return True
			if not s:
				return False
			if not t:
				return not pre
			this = s.val == t.val and dfs(s.left, t.left, True) and dfs(s.right, t.right, True)
			if pre:
				return this
			return this or dfs(s.left, t) or dfs(s.right, t)

		return dfs(s, t)
		

from Tree import BinaryTree

ss = [3,4,5,1,2]
tt = [3,4,5,1,2]#[4,1,2]

ss = [3,4,5,1,2]
tt = [1]

ss = [1,1]
tt = [1]

# ss = [3,4,5,1,2,'null','null',0]
# tt = [4,1,2]

# ss = [3,4,5,1,'null',2]
# tt = [3,1,2]

s = BinaryTree(ss).getTreeRoot()
t = BinaryTree(tt).getTreeRoot()

sl = Solution()
print( sl.isSubtree( s, t ) )