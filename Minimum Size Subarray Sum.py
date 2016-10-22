class Solution(object):
	def minSubArrayLen(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		length = len(nums)
		maxLength = length + 1 
		if not nums:
			return 0
		minLength = maxLength
		sumVal = nums[0]
		l = 0
		r = 1
		while l < r:
			if sumVal < s and r < length:
				sumVal = sumVal + nums[r]
				r += 1
			if sumVal >= s:
				if minLength > r-l:
					minLength = r-l
				sumVal = sumVal - nums[l]
				l = l + 1			
			elif r == length:
				break
		if minLength == maxLength: 
			return 0
		else:
			return minLength



		




s = 7
nums = [2,3,1,2,4,3,1,7]

sl = Solution()
print( sl.minSubArrayLen( s, nums ) )