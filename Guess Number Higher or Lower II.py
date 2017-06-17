import numpy
class Solution(object):
	def getMoneyAmount(self, n):
		"""
		:type n: int
		:rtype: int
		""" 
		need = [[0] * (n+1) for _ in range(n+1)]
		for lo in range(n, 0, -1):
			for hi in range(lo+1, n+1):
				need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
								   for x in range(lo, hi))
		print(numpy.array(need))
		return need[1][n]

	def online(self, n):
		def dfs( start, end):
			if start >= end:
				return 0

			if start + 1 == end:
				return start

			if record[start][end] is None:
				record[start][end] = min(
					i + max(dfs(start, i - 1), dfs(i + 1, end))
					for i in range(start, end + 1)
				)

			return record[start][end]

		record = [[None] * (n + 1) for _ in range(n + 1)]
		return dfs(1, n)





n = 5
sl = Solution()
print( sl.getMoneyAmount(n) )
print( sl.online(n) )


class Solution(object):
	def getMoneyAmount(self, n):s
		"""
		:type n: int
		:rtype: int
		""" 
		record = [ [None]*(n+1) for _ in range(n+1)]
		def dp(start, end):
			if start >= end:
				return 0
			if start == end + 2:
				return start
			if dp[start][end] is None:
				dp[start][end] = min(
					i + max(dp(start, i-1), dp(i+1, end)) for i in range(start,end+1))
			return record[start][end]
		return dp(1, n)