class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        maxVal = 0
        count = [1]*len(nums)
        for i in range( len(nums) ):
        	for j in range(0,i):
        		if nums[j]<nums[i]:
        			count[i] = max( count[i], count[j]+1 )
        	maxVal = max( count[i], maxVal )
        return maxVal



nums = [10, 9, 2, 5, 3, 7, 101, 18]
sl =Solution()
print( sl.lengthOfLIS(nums) )
print( sl.msl(nums) )