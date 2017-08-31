from itertools import combinations
from collections import Counter
class Solution(object):
	def validSquare(self, p1, p2, p3, p4):
		"""
		:type p1: List[int]
		:type p2: List[int]
		:type p3: List[int]
		:type p4: List[int]
		:rtype: bool
		"""
		counter = Counter()
		for (x1,y1), (x2,y2) in combinations([p1,p2,p3,p4], 2):
			distance = (x1-x2)**2 + (y1-y2)**2
			counter[distance] += 1
		if len(counter) != 2:
			return False
		vals = counter.values()
		if sorted(vals) != [2,4]:
			return False
		keys = counter.keys()
		if min(keys)*2 != max(keys):
			return False
		return True


	def online(self, p1, p2, p3, p4):
		def D( P, Q ):
			return (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2
		S = set(map(D, itertools.combinations((p1, p2, p3, p4), 2)))
		return len(S) == 2 and 0 not in S




p1, p2, p3, p4 = [0,0], [1,1], [1,0], [0,1]

sl = Solution()
print( sl.validSquare( p1, p2, p3, p4 ) )