class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        count = {}

        def dfs(root):
        	if root:
        		val = root.val + dfs(root.left) + dfs(root.right)
        		count[val] = count.get(val,0) + 1
        		return val
        	return 0

        dfs(root)
        maxVal = max(count.values())
        return [ i for i in count if count[i]==maxVal ]
        



t = [5,2,-5]
from Tree import BinaryTree

tree = BinaryTree(t)
root = tree.getRoot()

sl = Solution()
print( sl.findFrequentTreeSum( root ) )