# REVIEW: dp, edit distance

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [ [0]*(n+1) for _ in range(m+1) ]
        for i in range(m):
        	for j in range(n):
        		dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2*dp[-1][-1]




word1, word2 = "sea", "eat"
# word1, word2 = "ase", "sea"
# word1, word2 = "kitten", "sitting"
word1, word2 = 'a', 'a'
word1, word2 = "intention", "execution"

sl = Solution()
print( sl.minDistance( word1, word2 ) )