class Solution(object):
	def findShortestSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		dic = {}
		res, maxDegree = len(nums), 0
		for i, num in enumerate(nums):
			if num in dic:
				l, r, count = dic[num]
				count += 1
			else:
				l, r, count = i, i, 1
			dic[num] = [ l, i, count + 1 ]
			if count == maxDegree:
				res = min(res, i - l + 1)
			elif count > maxDegree:
				res = i - l + 1
				maxDegree = count
		return res



nums = [1,2,2,3,1,4,2]
nums = [1, 2, 2, 3, 1]
# nums = [2,1]
# nums = [2,1,1,2,1,3,3,3,1,3,1,3,2]

sl = Solution()
print( sl.findShortestSubArray( nums ) )