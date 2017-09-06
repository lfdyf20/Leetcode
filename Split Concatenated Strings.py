class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = [max(s, s[::-1]) for s in strs]
        return max( s[j:] + ''.join( strs[i+1:] + strs[:i] ) + s[:j]
        			for i, s in enumerate(strs)
        			for s in (s, s[::-1])
        			for j in range(len(s)) )
        



strs = ["abc", "xyz"]

sl = Solution()
print( sl.splitLoopedString( strs ) )