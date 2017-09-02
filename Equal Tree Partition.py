class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def update(node):
        	if not node:
        		return 0
        	node.val += update(node.left) + update(node.right)
        	return node.val

        target = update(root) / 2.0

        def check(node):
        	if node:
        		if node.val == target:
        			return True
        		return check(node.left) or check(node.right)
        	return False

        return check(root.left) or check(root.right)




nodes = '[5,10,10,null,null,2,3]'
from Tree import BinaryTree
tree = BinaryTree(nodes)
root = tree.getRoot()

sl = Solution()
print( sl.checkEqualTree( root ) )