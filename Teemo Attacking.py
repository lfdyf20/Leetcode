class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        count = 0
        timeSeries += [float('inf')]
        for i in range(1, len(timeSeries)):
        	count += min(duration, timeSeries[i] - timeSeries[i-1])
        return count



timeSeries, duration = [1,4], 2
timeSeries, duration = [1,2], 0

sl = Solution()
print( sl.findPoisonedDuration( timeSeries, duration ) )