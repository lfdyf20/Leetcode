class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        res = []

        def dfs(node, target, path):
        	if not node:
        		return

        	if not node.left and not node.right:
        		if target == node.val:
        			res.append(path + [node.val])
        		return

        	if node.left:
        		dfs( node.left, target - node.val, path + [node.val] )

        	if node.right:
        		dfs(node.right, target - node.val, path + [node.val])

        dfs(root, target, [])

        return res


vals = '[5,4,8,11,null,13,4,7,2,null,null,5,1]'

from Tree import BinaryTree
t = BinaryTree(vals)

root, target = t.getRoot(), 22

sl = Solution()
print( sl.pathSum( root, target ) )