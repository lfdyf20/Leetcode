class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        d = {}
        count = 0
        for i in range(len(p)):
        	if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i-1]) - ord(p[i]) == 25):
        		count += 1
        	else:
        		count = 1
        	d[ord(p[i])] = max(d.get(ord(p[i]), 0), count)
        return sum(d.values())



p = "zab"

sl = Solution()
print( sl.findSubstringInWraproundString( p ) )