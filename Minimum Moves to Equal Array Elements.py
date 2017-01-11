import numpy as np
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)
        # count = 0
        # step = 0
        # maxVal, minVal = max(nums), min(nums)
        # while maxVal != minVal and count<50:
        # 	count += 1
        # 	diff = maxVal - minVal
        # 	first = True
        # 	for i in range( len(nums) ):
        # 		if nums[i] == maxVal and first:
        # 			first = False
        # 			continue
        # 		nums[i] += diff
        # 	step += diff
        # 	maxVal, minVal = max(nums), min(nums)
        # 	# print( nums )
        # return step





nums = [3,1,4,1,5]
nums = [1,2,3]

sl = Solution()
print( sl.minMoves( nums ) )