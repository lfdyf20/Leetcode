class Solution(object):

	# REVIEW: different dp solution
	# FAVE: dp
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == s[::-1]:
        	return n
        dp = [[1] * n for _ in range(n)]
        for j in range(1, len(s)):
            for i in reversed(range(0, j)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][(j - 1)] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][(j - 1)])
        return dp[0][n-1]
        



s = "bbbab"
s = "cbbd"
# s = ""

sl = Solution()
print( sl.longestPalindromeSubseq( s ) )