class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def travel(root, label='right'):
            if root:
                if not root.left and not root.right:
                    if label == 'left':
                        return root.val
                    return 0
                return travel(root.left, 'left') + travel(root.right, 'right')
            return 0
        
        return travel(root)