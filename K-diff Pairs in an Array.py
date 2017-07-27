import collections
class Solution(object):
	def findPairs(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		if k < 0:
			return 0
		nums.sort()
		print(nums)
		n = len(nums)
		res = 0
		l, r = 0, 0
		count = 0
		while l < n:
			print("start: ", l, r)
			while l+1 < n and nums[l] == nums[l+1]:
				l += 1
				if l+1 >= n or nums[l] != nums[l+1]:
					count += 1
			print("left dup right: ", l)
			while r+1 < n and nums[l] + k > nums[r]:
				r += 1
			print("find r: ", r)
			if nums[l] + k == nums[r]:
				res += 1
			while r+1 < n and nums[r] == nums[r+1]:
				r += 1
			print("right dup right: ", r)
			
			l += 1
		return res if k else count


	def findPairs2(self, nums, k):
		if k>0:
			return len(set(nums)&set(n+k for n in nums))
		elif k==0:
			return sum(v>1 for v in collections.Counter(nums).values())
		else:
			return 0 


		


nums = [3,1,4,1,5,7,7,3]
# nums = [1]
nums = [1,3,1,5,4]
nums = [1,2,3,4,5]
# nums = [1,1,1,1,1]
k = 0

sl = Solution()
print( sl.findPairs(nums, k) )
print( sl.findPairs2(nums, k) )