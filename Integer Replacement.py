class Solution(object):

	memo = {}

	def integerReplacement(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n in self.memo:
			return self.memo[n]
		if n == 1:
			return 0
		if n%2 == 0:
			self.memo[n] = self.integerReplacement(int(n/2))+1
			return self.memo[n]
		else:
			self.memo[n] = min(self.integerReplacement(int(n+1)), self.integerReplacement(int(n-1)))+1
			return self.memo[n]
		   



n = 7

sl = Solution()
print( sl.integerReplacement( n ) )