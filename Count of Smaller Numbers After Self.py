import bisect

class Solution(object):
	def countSmaller0(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		res = [0] * len(nums)
		for i,l in enumerate(nums[:-1]):
			for r in nums[i+1:]:
				if r < l:
					res[i] += 1
		return res

	def countSmaller(self, nums):
		result = []
		sortedList = []
		for num in nums[::-1]:
			position=bisect.bisect_left(sortedList, num)
			result.append(position)
			bisect.insort(sortedList,num)
		return result[::-1]
		 
		



nums = [5, 2, 6, 1]

sl = Solution()
print( sl.countSmaller( nums ) )