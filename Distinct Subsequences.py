class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """ 
        dp = [ [1]*(len(s)+1) ] + [ [0]*(len(s)+1) for _ in range(len(t)) ]
        for ti in range(len(t)):
        	for si in range(len(s)):
        		if s[si] == t[ti]:
        			dp[ti+1][si+1] = dp[ti][si] + dp[ti+1][si]
        		else:
        			dp[ti+1][si+1] = dp[ti+1][si]
        return dp[-1][-1]
        



s, t = "rabbbit", "rabbit"

sl = Solution()
print( sl.numDistinct( s, t ) )