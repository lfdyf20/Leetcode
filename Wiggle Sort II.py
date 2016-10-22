class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		nums.sort()
		print(nums)
		half = len(nums[::2])
		print(nums[:half][::-1])
		print(nums[half:][::-1])
		nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]




nums = [1, 3, 2, 2, 3, 1, 9]
nums = [1,2,0,1]

sl = Solution()
print( sl.wiggleSort( nums ) )

print(nums)