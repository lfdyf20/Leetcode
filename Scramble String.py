class Solution(object):
	def isScramble(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: bool
		"""
		m, n = len(s1), len(s2)
		if m!=n or sorted(s1)!=sorted(s2):
			return False

		if n < 4 or s1 == s2:
			return True
			
		f = self.isScramble
		for i in range(1, n):
			if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
		   		f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
				return True
		return False


s1, s2 = "great", "etagr"

sl = Solution()
print( sl.isScramble( s1, s2 ) )