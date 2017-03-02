# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted( i.start for i in intervals )
        ends = sorted( i.end for i in intervals )
        
        e = 0
        numRooms = available = 0

        for start in starts:
        	while ends[e] <= start:
        		available += 1
        		e += 1
        	if available:
        		available -= 1
        	else:
        		numRooms += 1

        return numRooms




meetings = [[20,50],[0, 30],[5, 10],[15, 20]]
intervals = []
for start, end in meetings:
	intervals.append( Interval(start, end) )

sl = Solution()
print( sl.minMeetingRooms( intervals ) )