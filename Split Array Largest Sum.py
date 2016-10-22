class Solution(object):
	def splitArray(self, nums, m):
		"""
		:type nums: List[int]
		:type m: int
		:rtype: int
		"""
		if m == 1:
			return sum(nums)
		if m == len(nums):
			return max(nums)
		mean = sum( nums )/m
		# print(mean)
		minVal = float( 'inf' )
		for i in range(len(nums)-1):
			val = 0
			for j in range(i+1, len(nums)):
				if len(nums) - j + i < m-1:
					# print("not enough")
					# print( len(nums), j, i, m )
					break
				val = sum( nums[i:j] )
				# print(nums[i:j], val)
				if val > mean:
					# print(nums[i:j])
					minVal = min( val, minVal )
					break
		return minVal
		# minVal = float( 'inf' )
		# def travel(nums, m, minVal):
		# 	if m == 1:
		# 		return sum(nums)
		# 	for i in range(1, len(nums)-m):
		# 		print( nums[:i], nums[i:], m )
		# 		maxVal =  max( sum(nums[:i]), travel(nums[i:], m-1, minVal) )
		# 		minVal = min( minVal, maxVal )
		# travel( nums, m, minVal )
		# return minVal


nums = [1,2,3,4,5]
nums = [2,16,14,15]
m = 2

sl = Solution()
print( sl.splitArray( nums, m ) )