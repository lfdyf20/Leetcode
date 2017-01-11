from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls, lp = len(s), len(p)
        if lp > ls:
        	return []
        res = []
        cp = Counter(p)
        for i in range(ls-lp+1):
        	csi = Counter( s[i:i+lp] )
        	if csi == cp:
        		res.append(i)
        return res

    def fa(self, s, p):
    	pass




s, p = "cbaebabacd", "abc"
s, p = "abab", "ab"

sl = Solution()
print( sl.findAnagrams( s, p ) )
print( sl.fa(s, p) )