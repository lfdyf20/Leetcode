class Solution(object):
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		""" 
		subset = [[]]
		for i in nums:
			temp = []
			for j in subset:
				curr = sorted(j + [i])
				if curr in temp or curr in subset:
					continue
				else:   
				  temp.append(curr)
			subset = subset + temp
		return subset

	def subsetsWithDup2(self, nums):
		res = [[]]
		nums.sort()
		for i in range(len(nums)):
			if i == 0 or nums[i] != nums[i - 1]:
				length = len(res)
			for j in range(len(res) - length, len(res)):
				res.append(res[j] + [nums[i]])
		return res


nums = [2,1,2,1,3]
sl =Solution()
print( sl.subsetsWithDup(nums) )
print(len(sl.subsetsWithDup(nums)))


print( sl.subsetsWithDup2(nums) )