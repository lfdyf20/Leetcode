from tryFunc import timer
class Solution(object):

	@timer
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		
		def travel( target, nums ):
			if target == 0:
				return True
			if target < 0 or nums == []:
				return False
			if nums[0] > target:
				return False
			if nums[0] == target:
				return True
			return travel( target, nums[1:] ) or travel( target-nums[0], nums[1:] )
		n = sum(nums)
		nums.sort()
		if n%2 == 0:
			return travel( n//2, nums )
		return False

	@timer
	def cp( self, nums ):
		possible_sums = {0}
		for n in nums:
			possible_sums.update({(v + n) for v in possible_sums})
		return (sum(nums) / 2.)  in possible_sums

	@timer
	def mySolution(self, nums):
		target = sum(nums)//2
		if sum(nums)!=target*2:
			return False
		dp = [ [False]*(target+1) for _ in range(len(nums)+1)]
		dp[0][0]=True
		for i in range(1,len(dp)):
			for v in range(1,len(dp[i])):
				dp[i][v] = dp[i-1][v]
				if nums[i-1]<=v:
					dp[i][v] = dp[i][v] or dp[i-1][v-nums[i-1]]
		return any(dp[i][-1] for i in range(len(dp)))


nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]

sl = Solution()
# print( sl.canPartition( nums ) )
print( sl.cp( nums ))
print( sl.mySolution(nums) )