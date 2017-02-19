class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second = 0, 0
        res = 0
        hasZero = 0
        for i, num in enumerate(nums):
        	if num==0:
        		hasZero = 1
        		res = max(first + second + 1, res)
        		first, second = second, 0
        	else:
        		second += 1
        res = max(first + second + hasZero, res)
        return res

nums = [1]

sl = Solution()
print( sl.findMaxConsecutiveOnes( nums ) )