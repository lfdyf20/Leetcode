class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self.remove(root, key)

    def remove(self, node, key):
    	if not node:
    		return node
    	if node.val == key:
    		if not node.left and not node.right:
    			return None
    		if not node.left:
    			return node.right
    		if not node.right:
    			return node.left
    		node.val = self.findNewRootVal(node.left)
    		node.left = self.remove(node.left, node.val)
    	elif node.val > key:
    		node.left = self.remove(node.left, key)
    	else:
    		node.right = self.remove(node.right, key)
    	return node


    def findNewRootVal(self, node):
    	if node:
    		if node.right:
    			return self.findNewRootVal(node.right)
    		return node.val
    	return "ERROR"




vals, key = '[5,3,6,2,4,null,7]', 7
# vals, key = '[3,2,4,1]', 3

from Tree import BinaryTree
t = BinaryTree(vals)
root = t.getRoot()

sl = Solution()
newRoot =  sl.deleteNode( root, key )
t.drawTree(newRoot)