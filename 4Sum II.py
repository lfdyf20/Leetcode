import collections
class Solution(object):
	def fourSumCount(self, A, B, C, D):
		"""
		:type A: List[int]
		:type B: List[int]
		:type C: List[int]
		:type D: List[int]
		:rtype: int
		"""
		AB = collections.Counter(a+b for a in A for b in B)
		print(AB)
		print( [AB[-c-d] for c in C for d in D] )
		return sum(AB[-c-d] for c in C for d in D)




# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

A = [ -1, -1]
B = [-1,1]
C = [-1, 1]
D = [ 1, -1]

sl = Solution()
print( sl.fourSumCount( A, B, C, D ) )