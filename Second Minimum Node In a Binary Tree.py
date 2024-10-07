from Tree import TreeNode, BinaryTree
from typing import Optional

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = set()
        self.dfs( root, vals )
        if len(vals) < 2:
            return -1
        
        vals.remove( min(vals) )
        return min( vals )
    
    def dfs(self, root, vals: set):
        if not root:
            return
        
        if root.val not in vals:
            vals.add( root.val )
        
        self.dfs( root.left, vals )
        self.dfs( root.right, vals )

        




testcase = "[2,2,5,null,null,5,7]"
tree = BinaryTree(testcase)
root = tree.getRoot()

sl = Solution()
print( sl.findSecondMinimumValue( root ) )