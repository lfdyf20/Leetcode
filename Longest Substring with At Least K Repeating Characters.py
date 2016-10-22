import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
		"""
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)




s = "ababacb"
k =  3

sl = Solution()
print( sl.longestSubstring( s, k ) )