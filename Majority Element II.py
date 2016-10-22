from math import floor
class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		n = len(nums)
		if n <= 2:
			return list(set(nums))
		l = floor(n/3)
		print("n: ", n)
		print("n/3: ", l)
		res= []
		nums.sort()
		i = 0
		while i + l < n:
			if nums[i] == nums[i+l]:
				res += [nums[i]]
				print(res)
				i = i+l
			i = i + 1
		return res



nums = [1,1,1,2,2,2,3,3,3,3] 
nums = [1,2,3,4]
nums = [1,2,3],1
nums = [1]
sl = Solution()
print( sl.majorityElement( nums ) )