from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        curr, target = Counter(s2[:m]), Counter(s1)
        if target == curr:
        	return True
        for enter, leave in zip(s2[m:], s2):
        	curr[enter] += 1
        	curr[leave] -= 1
        	curr += Counter() # remove keys with 0 vals
        	if curr == target:
        		return True
        return False





s1= "ab"
s2 = "eidboaoo"

sl = Solution()
print( sl.checkInclusion( s1, s2 ) )