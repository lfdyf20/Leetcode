class Solution(object):
	def removeNDuplicates(self, nums, n):
		from collections import Counter
		counter = Counter(sorted(nums))
		res = []
		for i, num in sorted( counter.items() ):
			if num != n:
				res += [i]*num
		return res
	
	def remove2(self, nums, n):
		dic = {}
		res = []
		for i in nums:
			if i in dic:
				dic[i] += 1
			else:
				dic[i] = 1
		for i, num in sorted(dic.items()):
			if num != n:
				res += [i]*num
		return res



nums, n = [4,4,4,3,2,1,1], 3
# nums, n = [1,1,2,2,5,5,3,3], 1 

sl = Solution()
print( sl.removeNDuplicates( nums, n ) )
print( sl.remove2(nums, n) )