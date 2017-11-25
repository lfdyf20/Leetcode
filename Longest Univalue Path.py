class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        def dfs(node):
        	if not node: return 0
        	left_len, right_len = dfs(node.left), dfs(node.right)
        	left = (left_len + 1) if node.left and node.left.val == node.val else 0
        	right = (right_len + 1) if node.right and node.right.val == node.val else 0
        	self.longest = max( self.longest, left + right )
        	return max(left, right)

        dfs(root)
        return self.longest










from Tree import BinaryTree

vals = '[5,4,5,1,1,5]'
vals = '[1,4,5,4,4,null,5]'
# vals = '[1,1]'
vals = '[26,26,26,26,26,24,26,25,25,25,27,23,25,25,27,24,26,24,26,24,24,null,28,null,null,26,null,null,26,26,28,25,null,25,27,null,null,null,null,null,23,null,null,29,27,null,null,null,null,25,null,27,27,24,26,24,26,26,26,null,22,28,null,26,26,null,null,26,null,28,28,25,null,null,null,25,25,25,27,25,25,27,25,null,null,null,null,null,null,null,27,27,27,null,null,27,29,24,26,26,26,null,26,null,26,null,null,null,24,24,24,null,26,24,26,null,null,null,26,null,null,null,28,null,30,null,23,27,null,null,null,null,null,null,null,null,null,null,null,23,25,25,25,27,25,23,25,null,null,null,null,null,null,29,null,null,null,26,null,22,null,null,26,24,26,null,26,28,null,null,26,22,null,null,null,null,null,null,null,null,null,null,25,23,null,null,null,null,27]'

tree = BinaryTree( vals )
root = tree.getRoot()



sl = Solution()
print( sl.longestUnivaluePath( root ) )