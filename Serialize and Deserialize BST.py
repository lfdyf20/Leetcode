class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrder(root):
            if root:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)

        vals = []
        preOrder(root)
        return ''.join(vals)



    # REVIEW: build a BST tree from preorder
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = list(map(int, data.split()))
        vals.reverse()

        def build(minVal, maxVal):
            if vals and minVal <= vals[-1] <= maxVal:
                root = TreeNode(vals.pop())
                root.left = build(minVal, root.val)
                root.right = build(root.val, maxVal)
                return root

        return build(float('-inf'), float('inf'))
