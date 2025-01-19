

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
The binary search tree can be converted to a sorted (increasing) list by inorder traversal (left -> root -> right).

If swapping two tree node can make it a valid binary search tree, then there are two item in the list that are not in increasing order.
And what we need to do is to find these two items and swap them.

So where are these two items? 

Case 1: 1 4 3 2 5
We find the first incorrect item pair is 4 and 3, therefore the first item is 4.
We find the second incorrect item pair is 3 and 2, therefore the second item is 2.

Case 2: 5 2 3 1 5
We find the first incorrect item pair is 5 and 2, therefore the first item is 5.
We find the second incorrect item pair is 3 and 1, therefore the second item is 1.

In general, we can get two pairs of incorrect items, the first item is the first item of the first pair, the second item is the second item of the second pair.

What if the two incorrect items are adjacent?
Case 3: 1 3 2 4 5
We find the first incorrect item pair is 3 and 2, therefore the first item is 3.
There is no second incorrect item pair, therefore the second item is 2. This case tells us we need to refresh the second item whenever we find a new incorrect item pair.

Why we need a prev pointer?
This is because we need to compare the current node with the previous node to find the incorrect item pair. So after we finishing processing the current node, we need to update the prev pointer to the current node.

A general logic is:

def function():
    inorder_travel(root.left) # prev node can be updated

    # do something to the current node
    # compare the current node with the prev node
    # update the first and second item if needed
    # update the prev node to be the current node

    inorder_travel(root.right) # prev node will be used there

'''

class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None
        self.inorder( root )
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, node):
        if not node:
            return

        self.inorder( node.left )

        if self.prev and self.prev.val > node.val:
            if not self.first:
                self.first = self.prev
            self.second = node

        self.prev = node

        self.inorder( node.right )

    
        

from Tree import BinaryTree

vals = '[1,3,null,null,2]'
tree = BinaryTree( vals )

root = tree.getRoot()
# tree.drawTree()

sl = Solution()
sl.recoverTree( root )
tree.drawTree()