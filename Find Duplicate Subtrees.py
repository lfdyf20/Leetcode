from collections import defaultdict
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def tuplify(node):
        	if node:
        		tuple = root.val, tuplify(node.left), tuplify(node.right)
        		trees[tuple].append(root)
        		return tuple

        trees = defaultdict(list)

        tuplify(root)
        return [roots[0] for roots in trees.values() if roots[1:]]