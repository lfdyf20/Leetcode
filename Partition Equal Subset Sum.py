class Solution(object):
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

	def cp( self, nums ):
		possible_sums = {0}
		for n in nums:
			possible_sums.update({(v + n) for v in possible_sums})
		return (sum(nums) / 2.)  in possible_sums


nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]

sl = Solution()
# print( sl.canPartition( nums ) )
print( sl.cp( nums ))