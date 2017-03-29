class Solution(object):
	def twoClosestSum( self, nums ):
		nums.sort()
		res = float('inf')
		l, r = 0, len(nums)-1
		while r > l:
			print(nums[l], nums[r])
			val = nums[l] + nums[r]
			if abs(val-target) < abs(res-target):
				res = val
			if val == target:
				return target
			elif val > target:
				r -= 1
				while r > l and nums[r] == nums[r+1]:
					r -= 1
			else:
				l += 1
				while r > l and nums[l] == nums[l-1]:
					l += 1
		return res





nums = [1,1,1,1,2,3,7,10,9]
target = 14

sl = Solution()
print( sl.twoClosestSum(nums) )
