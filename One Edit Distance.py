class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s==t:
            return False
        ls, lt = len(s), len(t)
        if ls > lt:
            return self.isOneEditDistance( t, s)
        if lt - ls >1:
            return False
        for i in range( ls ):
            if s[i] != t[i]:
                if ls == lt:
                    s = s[:i] + t[i] + s[i+1:]
                else:
                    s = s[:i] + t[i] + s[i:]
                break
        return s == t or s == t[:-1]



s, t = "abc", "adc"

sl = Solution()
print( sl.isOneEditDistance( s, t ) )