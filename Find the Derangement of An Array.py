class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        x, y = 1, 0
        for i in range(1, n+1):
        	x, y = y, (i+1) * (x+y) % MOD
        return y



n = 10

sl = Solution()
print( sl.findDerangement( n ) )