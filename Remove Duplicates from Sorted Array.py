class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		res = len(nums)
		for i in range(  len( nums )-1, 0, -1 ):
			if nums[i] == nums[i-1]:
				nums.append( nums.pop(i) )
				res -= 1
		return res


	def mySolution(self, nums):
		res = len(nums)
		for i in range(1,len(nums)):
			if nums[~i] == nums[~(i-1)]:
				nums.append( nums.pop(~i) )
				res -= 1
		return resj


nums1 = [1,1]
nums2 = [1,1]
sample = Solution()
print(sample.removeDuplicates( nums1 ))
print(sample.mySolution(nums2))
print(nums1)
print(nums2)