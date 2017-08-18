from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hi = lo = 0
        counts = Counter()
        for hi in range(1, len(s)+1):
        	counts[ s[hi-1] ] += 1
        	mc = counts.most_common(1)[0][1]
        	if hi-lo-mc > k:
        		counts[s[lo]] -= 1
        		lo += 1
        return hi - lo



s = "AABABBA"
s = ""
k = 1

sl = Solution()
print( sl.characterReplacement( s, k ) )