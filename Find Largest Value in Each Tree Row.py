from Tree import BinaryTree
from tryFunc import timer

class Solution(object):
    @timer
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        if not root:
        	return
        thisLev, nextLev = [root], []
        res = []
        maxVal = root.val
        while thisLev or nextLev:
        	# print([node.val for node in thisLev], [node.val for node in nextLev])
        	if thisLev:
        		node = thisLev.pop()
        		if node.left:
        			nextLev.append(node.left)
        		if node.right:
        			nextLev.append(node.right)
        		maxVal = max(maxVal, node.val)
        	else:
        		# print(maxVal)
        		res.append(maxVal)
        		maxVal = float('-inf')
        		thisLev, nextLev = nextLev[:], []
        res.append(maxVal)
        return res
    
    @timer
    def online(self, root):
    	res = []
    	row = [root]
    	while any(row):
    		res.append( max(node.val for node in row) )
    		row = [ kid for node in row for kid in (node.left, node.right) if kid ]
    	return res







nodes = [1,3,2,5,3,"null",9]
nodes = [1,3,2,5,3,"null",9,11,3,2,"null",4]
tree = BinaryTree(nodes)


root = tree.getTreeRoot()

sl = Solution()
print( sl.largestValues( root ) )
print( sl.online(root) )