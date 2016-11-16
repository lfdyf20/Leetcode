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

    def nthUglyNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2,3,5]
        index, uglies = [0]*len(primes), [1]
        while len(uglies) < n:
            uglies.append( min( [p * uglies[index[i]] for i,p in enumerate( primes )] ) )
            for i, p in enumerate( primes ):
                if p * uglies[ index[i] ] == uglies[-1]:
                    index[i] += 1
        return uglies[-1]




n=10
sl=Solution()
print( sl.nthUglyNumber(n) )