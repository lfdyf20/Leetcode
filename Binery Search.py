import random
from math import floor
class Solution(object):
	def binerySearch(self, nums, target ):
		"""[summary]
		
		[description]
		
		Arguments:
			nums {[List[ number ]]} -- [description]
			target {[int]} -- [description]
		"""
		nums.sort()
		# trueVal = 0
		try:
			trueVal = nums.index(target)
		except Exception as e:
			pass
		else:
			pass
		finally:
			trueVal = "error"

		lo, hi = 0, len(nums)-1
		count = 0
		while lo < hi and count<1000:
			mid = (lo+hi) // 2 
			if nums[mid] < target:
				lo = mid+1 
			else:
				hi = mid 
			count += 1
		print( "count: ", count )
		val = hi
		print("True Value: ", trueVal)
		return lo







nums = [random.randint(0,200) for _ in range(100)]
nums =[2, 4, 4, 4, 7, 9, 13, 16, 19, 22, 23, 23, 24, 28, 28, 32, 32, 34, 36, 38, 44, 46, 46, 47, 48, 52, 52, 52, 53, 53, 58, 58, 60, 61, 62, 66, 67, 67, 69, 71, 71, 71, 76, 76, 77, 77, 82, 84, 85, 86, 91, 92, 94, 94, 99, 99, 100, 101, 101, 102, 102, 103, 108, 110, 115, 115, 121, 121, 122, 126, 126, 128, 129, 133, 133, 134, 135, 136, 137, 141, 142, 142, 151, 152, 154, 155, 155, 155, 155, 160, 164, 171, 172, 172, 175, 177, 180, 182, 182, 184, 191, 196]
nums = [1,4,4,6,7]
target = 5

sl = Solution()
print( sl.binerySearch(nums, target) )
		