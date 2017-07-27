class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
        	return ""
        if len(nums) == 1:
        	return nums[0]
        if len(nums) == 2:
        	return "/".join(map(str, nums))
        return str(nums[0]) + '/(' + '/'.join(map(str,nums[1:])) + ')'



nums = [1000,100,10,1]
nums = [100,10]
nums = []

sl = Solution()
print( sl.optimalDivision( nums ) )