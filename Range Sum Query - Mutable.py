class SegTreeNode(object):

    def __init__(self, lower, upper):
        self.left = None
        self.right = None
        self.total = 0
        self.lower = lower
        self.upper = upper



class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def createSegmentTree(nums, lower, upper):

            if lower > upper:
                return None

            if lower == upper:
                node = SegTreeNode(lower, upper)
                node.total = nums[lower]
                return node

            mid = (lower + upper) // 2

            root = SegTreeNode( lower, upper )
            root.left = createSegmentTree( nums, lower, mid )
            root.right = createSegmentTree( nums, mid+1, upper )

            root.total = root.left.total + root.right.total

            return root

        self.root = createSegmentTree( nums, 0, len(nums)-1 )
        
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        def updateVal(root, i, val):

            if root.lower == root.upper:
                root.total = val
                return val

            mid = (root.lower + root.upper) // 2

            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)

            root.total = root.left.total + root.right.total

            return root.total

        updateVal(self.root, i, val)


        
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def getSumVal(root, i, j):

            if root.lower == i and root.upper == j:
                return root.total

            mid = (root.lower + root.upper) // 2

            if j <= mid:
                return getSumVal(root.left, i, j)
            elif i >= mid + 1:
                return getSumVal(root.right, i, j)
            else:
                return getSumVal(root.left, i, mid) + getSumVal(root.right, mid+1, j)

        return getSumVal(self.root, i, j)
        
        


# Your NumArray object will be instantiated and called as such:
nums = [1,3,5]
obj = NumArray(nums)

i, val = 1, 2
obj.update(i,val)

i, j = 1, 2
param_2 = obj.sumRange(i,j)
print(param_2)