class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """ 
        n = len(nums)
        currSum = maxVal = sum(nums[:k])
        l, r = 0, k
        while r < n:
        	currSum = currSum - nums[l] + nums[r]
        	maxVal = max(maxVal, currSum)
        	l += 1
        	r += 1
        return maxVal/k



        



nums, k = [1,12,-5,-6,50,3], 4

sl = Solution()
print( sl.findMaxAverage( nums, k ) )