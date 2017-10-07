from collections import defaultdict
class Solution(object):
	def wordSquares(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[str]]
		"""
		n = len( words[0] )
		fulls = defaultdict(list)
		for word in words:
			for i in range(n):
				fulls[ word[:i] ].append( word )

		res = []

		def build( square ):
			if len(square) == n:
				res.append( square )
				return

			for word in fulls[ ''.join( list(zip(*square))[len(square)] ) ]:
				build(square + [word])

		for word in words:
			build( [word] )

		return res





words = ["area","lead","wall","lady","ball"]

sl = Solution()
print( sl.wordSquares( words ) )