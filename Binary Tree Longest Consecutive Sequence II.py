class Solution(object):
	def longestConsecutive(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0

		def dfs(root):
			if not root:
				return {"val":0, "up":float('-inf'), "down":float('-inf'), "child":float('-inf')}
				
			currDict = {"val": root.val}
			ld = dfs(root.left)
			rd = dfs(root.right)

			lup = ld["up"] + 1 if root.val - ld["val"] == 1 else 0
			rup = rd["up"] + 1 if root.val - rd["val"] == 1 else 0
			ldown = ld["down"] + 1 if root.val - ld["val"] == -1 else 0
			rdown = rd["down"] + 1 if root.val - rd["val"] == -1 else 0
			lchild = ld["child"]
			rchild = rd["child"]

			currDict["up"] = max(lup, rup, 1) 
			currDict["down"] = max(ldown, rdown, 1)
			currDict["child"] = max(lup + rdown - 1, ldown + rup - 1, lup, rup, ldown, rdown, lchild, rchild, 1)
			return currDict
			
		dict = dfs(root)
		return max(dict[key] for key in ["up", "down", "child"])



from Tree import BinaryTree
root = BinaryTree([3,1,"null","null",2]).getRoot()


sl = Solution()
print( sl.longestConsecutive( root ) )