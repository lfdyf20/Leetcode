class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for i in nums:
        	if i-1 not in nums:
        		n = i + 1
        		while n in nums:
        			n += 1
        		best = max( n-i, best )
        return best





nums = [100, 4, 200, 1, 3, 2]
sl = Solution()
print( sl.longestConsecutive( nums ) )