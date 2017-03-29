from tryFunc import timer

class Solution(object):
    @timer
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            for ind, j in enumerate(t):
                if j == i:
                    t = t[ind+1:]
                    break
            else:
                return False
        return True

    @timer
    def issub( self, s, t):

        t = iter(t)
        return all(c in t for c in s)




s, t = "abv", "abcedv"

sl = Solution()
print( sl.isSubsequence( s, t ) )
print( sl.issub(s, t) )