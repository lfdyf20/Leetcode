class Solution(object):
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		res = []
		self.travel( s, [], res )
		return res



	def travel(self, s, path, res):
		if s == "":
			res.append( path )
			return
		for i in range(len(s)):
			curr = s[:i+1]
			if curr == curr[::-1]:
				self.travel(s[i+1:], path+[curr], res)


	def online(self, s):
		return [ [s[:i] for i in range()] ]


	




	



s = "aaba"

sl = Solution()
print( sl.partition( s ) )
