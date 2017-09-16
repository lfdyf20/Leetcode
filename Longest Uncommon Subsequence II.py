class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSub(t, s):
        	t = iter(t)
        	return all(c in t for c in s)

        for s in sorted(strs, key=len, reverse=True):
        	if sum(isSub(t, s) for t in strs) == 1:
        		return len(s)

        return -1



strs = ["aba", "cdc", "eae"]

sl = Solution()
print( sl.findLUSlength( strs ) )