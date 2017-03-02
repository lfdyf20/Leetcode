from math import floor, ceil
class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		def search(n):
			lo, hi = 0, len(nums)
			while lo < hi:
				mid = ( lo + hi )//2
				if nums[mid] >= n:
					hi = mid
				else:
					lo = mid + 1
			return lo
		lo = search(target)
		return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]

	def mySolution(self, nums, target):
		def upperBs(num):
			lo, hi = 0 , len(nums)-1
			while lo < hi:
				mid = ceil((lo+hi)/2)
				if nums[mid] > num:
					hi = mid - 1
				else:
					lo = mid
			return hi

		def lowerBs(num):
			lo, hi = 0, len(nums)-1
			while lo < hi:
				mid = (lo+hi)//2
				if nums[mid] < num:
					lo = mid + 1
				else:
					hi = mid
			return lo


		hi = upperBs(target)
		lo = lowerBs(target)
		return [lo,hi] if target in nums[lo:hi] else [-1,-1]





nums, target = [5,7,7,8,8,10], 8

sl = Solution()
print( sl.searchRange( nums, target ) )
print( sl.mySolution(nums, target) )