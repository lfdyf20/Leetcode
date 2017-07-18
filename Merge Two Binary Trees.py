from Tree import BinaryTree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(t1, t2):
        	if not t1:
        		return t2
        	if not t2:
        		return t1
        	node = TreeNode(t1.val + t2.val)
        	node.left = merge(t1.left, t2.left)
        	node.right = merge(t1.right, t2.right)
        	return node

        return merge(t1, t2)

        



tree1 = [1,3,2,5]
tree2 = [2,1,3,'null',4,'null',7]

t1 = BinaryTree(tree1)
t2 = BinaryTree(tree2)

sl = Solution()
node = sl.mergeTrees( t1.getTreeRoot(), t2.getTreeRoot() )
print(t1.drawTree(node))