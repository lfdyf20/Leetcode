class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
        	return []
        n = len(nums)
        res = []
        for i in range(n-k+1):
        	res.append( max(nums[i:i+k]) )
        return res




nums, k = [1,3,-1,-3,5,3,6,7], 3

sl = Solution()
print( sl.maxSlidingWindow( nums, k ) )