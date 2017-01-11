class Solution(object):
	def splitArray(self, nums, m):
		"""
		:type nums: List[int]
		:type m: int
		:rtype: int
		"""
		def isValid(mid):
			count = 0
			current = 0
			for n in nums:
				current += n
				if current > mid:
					count += 1
					if count >= m:
						return False
					current = n
			return True

		l = max(nums)
		h = sum(nums)

		while l < h:
			mid = l + (h-l)//2
			if isValid(mid):
				print(mid)
				h = mid
			else:
				l = mid + 1
		return l




nums = [1,2,3,4,5]
nums = [2,16,14,15]
m = 2

sl = Solution()
print( sl.splitArray( nums, m ) )