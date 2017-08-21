class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = {0:1}
        curr = 0
        res = 0
        for num in nums:
        	curr += num
        	res += counter.get(curr - k, 0)
        	counter[curr] = counter.get(curr, 0) + 1
        return res



nums, k = [1,1,1], 2

sl = Solution()
print( sl.subarraySum( nums, k ) )