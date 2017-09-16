class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        stack = [root]
        res = []
        deep = -1
        while stack:
        	nextLevl, temp = [], []
        	for node in stack:
        		temp.append(node.val)
        		if node.left:
        			nextLevl.append(node.left)
        		if node.right:
        			nextLevl.append(node.right)
        	deep += 1
        	if deep % 2 == 0:
        		res.append( temp )
        	else:
        		res.append( list(reversed(temp)) )
        	stack = nextLevl
        return res





vals = '[3,9,20,null,null,15,7]' 
vals = '[1,2,3,4,null,null,5]'

from Tree import BinaryTree
t = BinaryTree(vals)
root = t.getRoot()

sl = Solution()
print( sl.zigzagLevelOrder( root ) )