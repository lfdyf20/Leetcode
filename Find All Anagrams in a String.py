from tryFunc import timer

from collections import Counter
class Solution(object):
    @timer
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

    @timer
    def fa(self, s, p):
    	ls, lp = len(s), len(p)
        if lp > ls:
            return []
        res = []
        cp = Counter(p)
        for i in range(ls-lp+1):
            if i == 0:
                cs = Counter(s[:lp])
            else:
                cs[s[i-1]] -= 1
                if not cs[s[i-1]]:
                    del cs[s[i-1]]
                cs[s[i+lp-1]] += 1
            # print(i, cp, cp, cs==cp)
            if cs == cp:
                res.append(i)
        return res





s, p = "cbaebabacd", "abc"
s, p = "abab", "ab"
s, p = "cbaebabacd", "abc"

sl = Solution()
print( sl.findAnagrams( s, p ) )
print( sl.fa(s, p) )