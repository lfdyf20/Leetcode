import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """ 
        return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))
        res = [[0]*n]*m
        for i in range( m ):
        	for j in range( n ):
        		if i==0 and j==0:
        			res[i][j] = 1
        		elif i==0:
        			res[i][j] = res[i][j-1]
        		elif j==0:
        			res[i][j] = res[i-1][j]
        		else:
        			res[i][j] = res[i][j-1] + res[i-1][j]
        return res[-1][-1]




m, n = 3, 2


sl = Solution()
print( sl.uniquePaths( m, n ) )

