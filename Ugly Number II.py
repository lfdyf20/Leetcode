from heapq import *
from tryFunc import timer
class Solution(object):
    @timer
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

    @timer
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


    @timer
    def mySolution(self, n):
        if n <= 5:
            return [1,2,3,4,5][n-1]
        m = 5
        rec = set( [1,2,3,4,5] )
        num = 6
        while True and num < 100000:
            for i in [2,3,5]:
                if num % i == 0 and num//i in rec:
                    m += 1
                    rec.add( num )
                    if m==n:
                        return num
                    break
            num += 1




n=1000
sl=Solution()
print( sl.nthUglyNumber(n) )
print( sl.nthUglyNumber2(n) )
print( sl.mySolution(n) )
