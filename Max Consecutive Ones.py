class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = 0
        prior = 0
        for i,num in enumerate(nums):
        	if num == 0:
        		maxVal = max(maxVal, i-prior)
        		prior = i+1
        maxVal = max(maxVal, i+1-prior)
        return maxVal



nums = [1,1,0,1,1,1,0]

sl = Solution()
print( sl.findMaxConsecutiveOnes( nums ) )

a = []
pr