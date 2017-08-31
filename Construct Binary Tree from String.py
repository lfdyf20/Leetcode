# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
	def str2tree(self, s):
		"""
		:type s: str
		:rtype: TreeNode
		"""
		l = s.find("(")
		if l < 0:
			return TreeNode(int(s)) if s else None
		count = 1
		for r in range(l+1, len(s)):
			if s[r] == "(": count += 1
			elif s[r] == ")": count -= 1
			if count == 0:
				break

		root = TreeNode(int(s[:l]))
		root.left = self.str2tree(s[l+1:r])
		root.right = self.str2tree(s[r+2:-1])
		return root


	def onlineHack(self, s):
		def t(val, left=None, right=None):
			node, node.left, node.right = TreeNode(val), left, right
			return node
		return eval('t(' + s.replace('(', ',t(') + ')') if s else None


s = "4(2(3)(1))(6(5))"

sl = Solution()
print( sl.str2tree( s ) )