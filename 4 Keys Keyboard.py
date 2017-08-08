class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [i for i in range(N+1)]
        for i in range(1, N+1):
        	for j in range(1, i):
        		if j+3 <= i:
        			dp[i] = max(dp[i], dp[j]*(i-j-1))
       	return dp[-1]




N = 10

sl = Solution()
print( sl.maxA( N ) )