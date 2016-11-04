class Solution(object):
	def minPatches(self, nums, n):
		"""
		:type nums: List[int]
		:type n: int
		:rtype: int
		"""
		# sumVal = []
		# for i in range(1,n+1):
		i, k, added = 0,0,0
		while k < n:
			if i < len(nums) and nums[i] <= k+1:
				k += nums[i]
				i+=1
			else:
				k += k+1
				added += 1
		return added



nums, n = [1, 5, 10], 20

sl = Solution()
print( sl.minPatches( nums, n ) )