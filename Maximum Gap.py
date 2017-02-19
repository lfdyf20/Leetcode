import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum, minNum = max(nums), min(nums)
        size = math.ceil((maxNum - minNum)//(len(nums)-1))
        buckets = [[None, None] for _ in range((maxNum-minNum)//size+1)]
        for num in nums:
        	b = buckets[(num-minNum)//size]
        	b[0] = num if b[0] is None else mn(b[0], num)
        	b[1] = num if b[1] is None else max(b[1], num)
        buckets = [b for b in buckets if b[0] is not None]
        return max(buckets[i][0]-buckets[i-1][1] for i in range(1, len(buckets)))




nums = [3,1,4,9,1,5,26]

sl = Solution()
print( sl.maximumGap( nums ) )