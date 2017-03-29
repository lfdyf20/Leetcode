class Solution(object):
	def sumAndAverage(self, nums):
		print(nums[::2])
		if not nums:
			return
		sumVal = sum( nums[::2] )
		avVal = sumVal/(len(nums[::2]))
		return sumVal, avVal

	def solution2(self, nums):
		if not nums:
			return
		res, count = 0, 0 
		for i in range(0,len(nums), 2):
			res += nums[i]
			count += 1
		return res, res/count



nums = [-1,-2]

sl = Solution()
print( sl.sumAndAverage( nums ) )
print( sl.solution2(nums) )