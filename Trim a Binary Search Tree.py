class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
        	return None
        if root.val < L:
        	return self.trimBST(root.right, L, R)
        elif root.val > R:
        	return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L ,R)
        root.right = self.trimBST(root.right, L, R)
        return root



# generate a binary tree using vals as pre-order
from Tree import BinaryTree

vals = '[1,0,2]'

tree = BinaryTree( vals )
root = tree.getRoot()

L, R = 1, 2

sl = Solution()
print( sl.trimBST( root, L, R ) )