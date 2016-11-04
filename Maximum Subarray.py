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

    def ms( self, nums ):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        maxVal = nums[0]
        for i in nums[1:]:
            temp = max(0, temp)
            temp += i
            maxVal = max( i , temp, maxVal )
        return maxVal



# nums = [-1,1,2,1]
nums = [-2,1,3,1,4,-1,-5,4,-39,12]
sample = Solution()
print( sample.ms(nums) )
print( sample.maxSubArray(nums) )

