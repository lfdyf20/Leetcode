from typing import Optional
from Tree import BinaryTree
from BinaryTree import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST( root.right, val )
        return self.searchBST( root.left, val )


nodes = "[4,2,7,1,3]"
tree = BinaryTree(nodes)
root = tree.getRoot()

val = 10
sl = Solution()
print( str(sl.searchBST( root, val )) )