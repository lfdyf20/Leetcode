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

	def mySolution(self, nums):
		nums.sort()
		res = [[]]
		for i, num in enumerate(nums):
			if i>0 and num == nums[i-1]:
				res += [ res[-1] + [num] ]
				continue
			res += [ pre + [num] for pre in res ]
		return res


	def online(self, nums):
	    res = []
	    nums.sort()
	    self.dfs(nums, 0, [], res)
	    return res
	    
	def dfs(self, nums, index, path, res):
	    res.append(path)
	    for i in xrange(index, len(nums)):
	        if i > index and nums[i] == nums[i-1]:
	            continue
	        self.dfs(nums, i+1, path+[nums[i]], res)

nums = [2,1,2,1,3,4,6,3]
nums = [0]
nums = [5,5,5,5,5]
sl =Solution()
print( sl.subsetsWithDup(nums) )
print(len(sl.subsetsWithDup(nums)))


print( sl.subsetsWithDup2(nums) )
print(len(sl.subsetsWithDup2(nums)))

print( sl.mySolution(nums) )
print( len(sl.mySolution(nums)) )