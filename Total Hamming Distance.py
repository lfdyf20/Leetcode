class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum( b.count('1')*b.count('0') for b in zip(*map('{:032b}'.format, nums) ))



nums = [4,14,2]

sl = Solution()
print( sl.totalHammingDistance( nums ) )