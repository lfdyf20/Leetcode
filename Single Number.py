class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        nums.sort()
        check = []
        for i in nums:
        	if i not in check:
        		check.append( i )
        	else:
        		check.pop()
        return check




nums = [1,2,1,3,2,5] 
sample = Solution()
print sample.singleNumber(nums)
