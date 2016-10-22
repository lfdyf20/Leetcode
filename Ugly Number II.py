from heapq import *
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        h = [1]
        i = 0
        s =set()
        while i <n :
        	e = heappop(h)
        	if e not in s:
        		s.add(e)
        		heappush(h, e*2)
        		heappush(h, e*3)
        		heappush(h, e*5)
        		i += 1
        return e




n=10
sl=Solution()
print( sl.nthUglyNumber(n) )