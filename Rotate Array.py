class Solution(object):
	# def rotate(self, nums, k):
	#     """
	#     :type nums: List[int]
	#     :type k: int
	#     :rtype: void Do not return anything, modify nums in-place instead.
	#     """ 
	#     k = min(k, len(nums))
	#     reversePart = nums[len(nums)-k:]
	#     reversePart.reverse()
	#     nums = nums[: len(nums)-k] + reversePart
	#     print nums
	#     # print type(nums[:len(nums)-k]), type(nums[len(nums)-k:].reverse())
	#     # nums = nums[:len(nums)-k] + nums[len(nums)-k:].reverse()
	def rotate(self, nums, k):
		# k = min(k, len(nums))
		# print(nums[len(nums)-k:])
		# temp = nums[len(nums)-k:] + nums[: len(nums)-k]
		# print(nums)
		k = min( len(nums), k )
		for _ in range(k):
			nums.insert(0, nums.pop())



nums = [1,2]
k = 1
sample = Solution()
sample.rotate(nums, k)
print(nums)