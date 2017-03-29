from collections import Counter
class Solution(object):
	def findSecMostFrequentNumber(self, nums):
		counter = Counter(nums)
		freq = sorted(list(set(counter.values())), reverse=True)[1]
		res = []
		for num, f in counter.items():
			if f == freq:
				res.append(num)
		return res

	def solution2(self, nums):
		return Counter(nums).most_common(2)[1][0]





nums = [3,1,4,1,3,5,1,3,4,2,2,3,4]
print(Counter(nums))
sl = Solution()
print( sl.findSecMostFrequentNumber( nums ) )
print( sl.solution2( nums ) )