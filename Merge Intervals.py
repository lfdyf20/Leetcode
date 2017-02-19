# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals.sort(key = lambda x: x.start)
        for i in intervals:
        	if not res or i.start > res[-1].end:
        		res.append(i)
        		continue
        	if i.start <= res[-1].end and i.end >res[-1].end:
        		interval = Interval(res[-1].start, i.end)
        		res[-1] = interval
        return res







intervalList = [[2,6],[1,3],[8,9],[8,10],[15,18]]
intervals = []
for ele in intervalList:
	intervals.append( Interval(ele[0],ele[1]) )


sl = Solution()
res =  sl.merge( intervals )
output = []
for i in res:
	output.append( [i.start, i.end] )
print(output)