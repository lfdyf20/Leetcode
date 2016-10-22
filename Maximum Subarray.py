class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        maxVal = nums[0]
        for i in range(1, len(nums)):
        	nums[i] = max( nums[i], nums[i]+nums[i-1] )
        	if nums[i] > maxVal:
        		maxVal = nums[i]
        return maxVal




nums = [-2,1,-3,4,-1,2,1,-5,4]
sample = Solution()
print( sample.maxSubArray(nums) )
# print( sample.maxToEnd( nums ))
# print( len(nums) )
