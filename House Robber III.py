from Tree import BinaryTree

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
        	if not root:
        		return (0, 0)
        	l0, l1 = dfs(root.left)
        	r0, r1 = dfs(root.right)
        	return (max(l1,l0)+max(r0,r1),  l0+r0+root.val)

        return max(dfs(root))



vals = [3,2,3,'null',3,'null',1]
vals = [3,4,5,1,3,'null',1]

tree = BinaryTree(vals)
root = tree.getRoot()

sl = Solution()
print( sl.rob( root ) )