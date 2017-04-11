from tryFunc import timer

class Solution(object):

	res = 0
	
	@timer
	def findTargetSumWays(self, nums, S):
		"""
		:type nums: List[int]
		:type S: int
		:rtype: int
		"""
		
		def dfs(nums, target):
			if not nums:
				if target == 0:
					self.res += 1
				return
			dfs(nums[1:], target+nums[0])
			dfs(nums[1:], target-nums[0])

		dfs(nums, S)
		return self.res

	@timer
	def mysolution(self, nums, S):
		dic = {0:1}
		for x in nums:
			tempDic = {}
			for tempSum in dic:
				tempDic[ tempSum+x ] = tempDic.get(tempSum+x, 0) + dic[tempSum]
				tempDic[ tempSum-x ] = tempDic.get(tempSum-x, 0) + dic[tempSum]
			dic = tempDic
		return dic.get(S,0)





nums, S = [1, 1, 1, 1, 1], 3

sl = Solution()
print( sl.findTargetSumWays( nums, S ) )
print( sl.mysolution(nums, S) )