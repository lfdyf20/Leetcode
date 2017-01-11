import re
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        d = [False] * len(s)
        for i in range( len(s) ):
            for w in wordDict:
                if w == s[i-len(w)+1: i+1] and ( d[i-len(w)] or i-len(w) == -1 ):
                    d[i]=True
        return d[-1]



s, wordDict = "leetcode", ["leet", "code"]

sl = Solution()
print( sl.wordBreak( s, wordDict ) )