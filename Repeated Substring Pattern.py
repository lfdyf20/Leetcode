class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]



s = "abcabcabcabc"

sl = Solution()
print( sl.repeatedSubstringPattern( s ) )