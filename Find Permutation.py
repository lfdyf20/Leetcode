class Solution(object):
	def findPermutation(self, s):
		"""
		:type s: str
		:rtype: List[int]
		"""
		res = []
		for i in range(len(s)):
			if s[i] == 'I':
				res.extend( range(i+1, len(res), -1) )
		res.extend( range(len(s)+1, len(res), -1) )
		return res

		


s = "DIDDDIDDDDD"
s = "D"

sl = Solution()
print( sl.findPermutation( s ) )