# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        orders = self.inorder(root)
        return min( orders[i]-orders[i-1] for i in range(1, len(orders)) )
        
        
    def inorder(self,root):
        return self.inorder(root.left)+[root.val]+self.inorder(root.right) if root else []