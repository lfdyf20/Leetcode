class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		s_bianma = self.bianma(s)
		t_bianma = self.bianma(t)
		return s_bianma == t_bianma

	def bianma(self, k):
		"""
		:type k: str
		:rtype : list
		"""
		t = 0
		memo = {}
		shuzi = []
		for i in k:
			if memo.has_key(i):
				shuzi.append(memo.get(i))
			else:
				memo[i] = t
				t = t + 1
				shuzi.append(t)
		return shuzi


solution = Solution()
s = 'ab'
t = 'aa'
print bool(solution.isIsomorphic(s,t))