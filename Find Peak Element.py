class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        if len(nums) == 1:
        	return 0
        if nums[0]>nums[1]:
        	return 0
        if nums[-1]>nums[-2]:
        	return len(nums)-1
        for i in range(1,len(nums)-1):
        	if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
        		return i
        return None
        




nums = [1,2]
sl = Solution()
print( sl.findPeakElement(nums) )