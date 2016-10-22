class Solution(object):
	def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		""" 
		first = second = float('inf')
		for n in nums:
			if n <= first:
				first = n
			elif n <= second:
				second = n
			else:
				return True
		return False





nums = [4,8,2,7,7]
sl = Solution()
print( sl.increasingTriplet(nums) )