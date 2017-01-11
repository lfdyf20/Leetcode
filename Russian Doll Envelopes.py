from bisect import bisect_left
class Solution(object):
	def maxEnvelopes(self, envelopes):
		"""
		:type envelopes: List[List[int]]
		:rtype: int
		"""
		es = [ e[1] for e in sorted( envelopes, key=lambda x: (x[0], -x[1]))]
		res = []
		for e in es:
			pos = bisect_left( res, e )
			if pos >= len(res):
				res.append( e )
			else:
				res[pos] = e
		return len(res)
		


envelopes = [[5,4],[6,4],[6,7],[2,3],[3,7], [5,6], [1,6]]
# envelopes = [[1,6],[2,8],[3,3],[4,4]]

sl = Solution()
print( sl.maxEnvelopes( envelopes ) )