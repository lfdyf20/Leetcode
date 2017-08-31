from DecoratorHelper import timer

# TODO: try all sort algorithm
class Solution(object):
	@timer
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		""" 
		return sorted(nums)[-k]

	@timer
	def mySolution(self, nums, k):
		from heapq import heappushpop, heappush, heappop
		import heapq
		# stack = []
		# for num in nums:
		# 	if len(stack) < k:
		# 		heappush(stack, num)
		# 	else:
		# 		heappushpop(stack, num)
		# return heappop(stack)
		return heapq.nlargest(k, nums)[k-1]

		



nums = [1,3,5,7,8]
k = 2
sl =Solution()
print( sl.findKthLargest(nums, k) )
print( sl.mySolution(nums, k) )