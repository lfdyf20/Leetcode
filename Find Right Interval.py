from collections import defaultdict
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from bisect import bisect
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        starts = sorted([ I.start, ind ] for ind, I in enumerate(intervals)) + [[float('inf'), -1]]
        return [starts[bisect(starts, [I.end])][-1] for I in intervals]



x = [ [1,2] ]
x = [ [3,4], [2,3], [1,2] ]
x = [ [0,1], [2,3], [3,4] ]
intervals = []
for i,j in x:
	intervals.append( Interval(i,j) )

sl = Solution()
print( sl.findRightInterval( intervals ) )