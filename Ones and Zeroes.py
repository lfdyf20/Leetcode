class Solution(object):
	def findMaxForm(self, strs, m, n):
		"""
		:type strs: List[str]
		:type m: int
		:type n: int
		:rtype: int
		"""
		dp = [ [0]*(n+1) for _ in range(m+1) ]

		def count(s):
			return sum(1 for c in s if c=='0'), sum(1 for c in s if c=='1')

		for z,o in [ count(s) for s in strs ]:
			for i in range(m, -1, -1):
				for j in range(n, -1, -1):
					if i >= z and j >= 0:
						dp[i][j] = max( dp[i][j], dp[i-z][j-o]+1 )

		return dp[m][n]


strs, m, n = ["10", "0001", "111001", "1", "0"], 5,3

sl = Solution()
print( sl.findMaxForm( strs, m, n ) )