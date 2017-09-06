class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
        	return
        stack = [ root ]
        res = []
        while stack:
        	node = stack.pop()
        	stack += [child for child in (node.right, node.left) if child]
        	res.append(node)

        for nl, nr in zip(res, res[1:]):
        	nl.left, nl.right = None, nr



from Tree import BinaryTree
vals = '[1,2,5,3,4,null,6]'
# vals = '[1]'
vals = '[1,2,null,3,4,5]'
t = BinaryTree(vals) 

root = t.getRoot()

sl = Solution()
sl.flatten( root )
t.drawTree( root )


"""Leetcode discussion

class Solution:
# @param root, a tree node
# @return nothing, do it in place
prev = None
def flatten(self, root):
    if not root:
        return
    self.prev = root
    self.flatten(root.left)

    temp = root.right
    root.right, root.left = root.left, None
    self.prev.right = temp

    self.flatten(temp)
""" 
