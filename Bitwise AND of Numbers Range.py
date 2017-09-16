class Solution(object):
	def rangeBitwiseAnd(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		i = 0
		while m != n:
			m >>= 1
			n >>= 1
			i += 1
			print(bin(m), bin(n))
		return n << i



m, n = 5, 11

sl = Solution()
print( sl.rangeBitwiseAnd( m, n ) )