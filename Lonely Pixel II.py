import collections

class Solution(object):
	def findBlackPixel(self, picture, N):
		"""
		:type picture: List[List[str]]
		:type N: int
		:rtype: int
		"""
		rowCounter = collections.Counter(map(tuple, picture))
		cols = [ col.count('B') for col in zip(*picture) ]
		return sum( N * list(zip(row, cols)).count(('B', N))
				for row, count in rowCounter.items()
				if count == N == row.count('B'))



picture, N = ["WBWBBW","WBWBBW","WBWBBW","WWBWBW"], 3

sl = Solution()
print( sl.findBlackPixel( picture, N ) )