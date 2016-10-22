class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal = maxVal = maxRes = nums[1]
        for i in range(1, len(nums)):
        	minVal = min( nums[i], nums[i]*minVal, nums[i]*maxVal )
        	maxVal = max( nums[i], nums[i]*minVal, nums[i]*maxVal )
        	maxRes = max( maxVal, maxRes )
        return maxRes






nums = [2,-5,-2,-4,3]
# nums = [7,-2,-4]
nums = [1,2,3,-4,2,3,4,-1,-1]
nums =[-1,-2,-9,-6]

sl = Solution()
print( sl.maxProduct( nums ) )

