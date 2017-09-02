class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []

        def dfs(node, val):
        	if node:
        		curr = val*10 + node.val
        		if not node.left and not node.right:
        			vals.append( curr )
        			return
        		dfs(node.left, curr)
        		dfs(node.right, curr)

        dfs(root, 0)
        return sum(vals)





vals = '[1,2,3,4]'
from Tree import BinaryTree
t = BinaryTree(vals)

root = t.getRoot() 
sl = Solution()
print( sl.sumNumbers( root ) )