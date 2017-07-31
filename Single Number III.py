class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
        	xor ^= num
        a = 0
        b = 0
        firstDiff = 1
        while firstDiff & xor == 0:
        	firstDiff = firstDiff << 1

        for num in nums:
        	if num & firstDiff == 0:
        		a ^= num
        	else:
        		b ^= num
        return [a, b]



nums = [1, 2, 1, 3, 2, 5]

sl = Solution()
print( sl.singleNumber( nums ) )