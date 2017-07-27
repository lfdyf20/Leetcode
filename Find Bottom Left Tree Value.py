from collections import deque

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        stack = deque([root])
        while stack:
        	leftmost = stack[0]
        	temp = deque([])
        	while stack:
        		node = stack.popleft()
        		temp += [child for child in (node.left, node.right) if child]
        	if not temp:
        		return leftmost.val
        	stack = temp

    def online(self, root):
    	queue = [root]
    	for node in queue:
    		queue += filter(None, (node.right, node.left))
    	else:
    		return node.val




from Tree import BinaryTree

t = [1,2,3,4,'null',5,6,'null','null',7]
tree = BinaryTree(t)
root = tree.getTreeRoot()


sl = Solution()
print( sl.findBottomLeftValue( root ) )