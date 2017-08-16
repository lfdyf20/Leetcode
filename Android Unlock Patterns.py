class Solution(object):
	# REVIEW: matrix 
	def numberOfPatterns(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		skip = [[0]*10 for _ in range(10)]
		skip[1][3] = skip[3][1] = 2
		skip[1][7] = skip[7][1] = 4
		skip[3][9] = skip[9][3] = 6
		skip[7][9] = skip[9][7] = 8
		skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
		visited = set()
		res = 0

		def dfs(curr, remain):
			if remain < 0:
				return 0
			if remain == 1:
				return 1
			visited.add(curr)
			tempRes = 0
			for i in range(1, 10):
				if not i in visited and (skip[curr][i]==0 or skip[curr][i] in visited):
					tempRes += dfs(i, remain-1)
			visited.remove(curr)
			return tempRes

		for i in range(m, n+1):
			res += dfs(1, i) * 4
			res += dfs(2, i) * 4
			res += dfs(5, i)
		return res


m, n = 2,3

sl = Solution()
print( sl.numberOfPatterns( m, n ) )