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


	def mySolution(self, s, nums):
		total = left = 0
		res = len(nums) + 1
		for right, n in enumerate(nums):
			total += n
			while total >= s:
				res = min(res, right - left + 1)
				total -= nums[left]
				left += 1
		return res if res <= len(nums) else 0







s = 7
nums = [2,3,1,2,4,3,1,7]
# nums = [2,3,1,2,4,3]

sl = Solution()
print( sl.minSubArrayLen( s, nums ) )
print( sl.mySolution(s, nums) )
# print( sl.msa( s, nums ) )s