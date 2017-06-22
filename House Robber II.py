class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dp(nums):
        	memo = [0] * (len(nums)+1)
        	memo[1], memo[2] = nums[0], nums[1]
        	for i in range(3, len(nums)+1):
        		memo[i] = max(memo[i-2], memo[i-3]) + nums[i-1]
        	print(memo)
        	return max(memo[-1], memo[-2])
        if not nums:
        	return 0
        if len(nums)<=3:
        	print('length')
        	return max(nums)
        return max(dp(nums[:-1]), dp(nums[1:]))




nums = []

sl = Solution()
print( sl.rob( nums ) )