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


nums = [2,1,2,1,3]
sl =Solution()
print( sl.subsetsWithDup(nums) )
print(len(sl.subsetsWithDup(nums)))