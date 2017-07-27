from Tree import BinaryTree

import re
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def dfs(root):
        	if root:
        		return "{}({})({})".format(root.val, dfs(root.left), dfs(root.right))
        	return ""

        res = dfs(t)
        print(res)
        res = re.sub(r"\(\)\(\)", "", res)
        res = re.sub(r"\(\)\)", ")", res)
        res = re.sub(r"\(\)$", "", res)
        print(res)
        return res



l = [1,2,3,4]
l = [1,2,3,'null',4]
l = [1,2,'null',3,4]

t = BinaryTree(l)
# print(t)

sl = Solution()
print( sl.tree2str( t.getTreeRoot() ) )