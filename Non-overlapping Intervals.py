# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def eraseOverlapIntervals(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: int
		"""
		end = float('-inf')
		ct = 0
		for i in sorted( intervals, key=lambda x: x.end ):
			if i.start >= end:
				end = i.end
			else:
				ct += 1
		return ct    



x = [ [1,2], [2,3], [3,4], [1,3]]
intervals = []
for i,j in x:
	intervals.append( Interval(i,j) )

sl = Solution()
print( sl.eraseOverlapIntervals( intervals ) )