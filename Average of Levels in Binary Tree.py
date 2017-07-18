class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
        	return []
        result = []
        stack = [root]
        temp = []
        while stack:
        	sumVal, count = 0, 0
        	while stack:
        		node = stack.pop()
        		temp += [child for child in (node.left, node.right) if child]
        		sumVal += node.val
        		count += 1
        	stack, temp = temp, []
        	result.append(sumVal/count)
        return result






from Tree import BinaryTree
root = [3,9,20,15,7]
tree = BinaryTree(root)

sl = Solution()
print( sl.averageOfLevels( tree.getTreeRoot() ) )