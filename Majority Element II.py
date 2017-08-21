from math import floor
class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		f, s = 0, 1
		fc = sc = 0
		for num in nums:
			if num == f:
				fc += 1
			elif num == s:
				sc += 1
			elif fc == 0:
				f, fc = num, 1
			elif sc == 0:
				s, sc = num, 1
			else:
				fc -= 1
				sc -= 1

		fl = sum(1 for num in nums if num == f)
		sl = sum(1 for num in nums if num == s)
		res = []
		if fl > len(nums)//3:
			res += [f]
		if sl > len(nums)//3:
			res += [s]
		return res




nums = [1,1,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3] 
# nums = [1,2,3,4]
# nums = [1,2,3],1
# nums = [1]
nums = [8,8,8,8]
sl = Solution()
print( sl.majorityElement( nums ) )