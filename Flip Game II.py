class Solution(object):
	def canWin(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		return any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:])
				   for i in range(len(s)))
	
	_memo = {}
	def online(self, s):
		
		memo = self._memo
		if s not in memo:
			memo[s] = any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:])
						  for i in range(len(s)))
		return memo[s]



s = "++++++"

sl = Solution()
print( sl.canWin( s ) )
print( sl.online(s) )