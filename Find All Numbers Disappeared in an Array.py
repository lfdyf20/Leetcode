class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
        	nums[abs(i)-1] = min(nums[abs(i)-1], -nums[abs(i)-1])
        for i, num in enumerate(nums):
        	if num > 0:
        		res.append( i+1 )
        return res


nums = [4,3,2,7,8,2,3,1]
nums = [2,2]

sl = Solution()
print( sl.findDisappearedNumbers( nums ) )