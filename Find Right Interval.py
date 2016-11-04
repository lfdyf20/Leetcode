from collections import defaultdict
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        dic = defaultdict(lambda: -1)
        for ind, interval in enumerate(intervals):
        	dic[ interval.start ] = ind
        print(dic)
        res = []
        for i in intervals:
        	res.append( dic[ i.end ] )
        return res



x = [ [1,2] ]
intervals = []
for i,j in x:
	intervals.append( Interval(i,j) )

sl = Solution()
print( sl.findRightInterval( intervals ) )