class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        res = sum(map(ord, t)) - sum(map(ord, s))
        resChar = chr(res)
        return resChar




s = "abc"
t = "bcae"
sl = Solution()
print( sl.findTheDifference(s,t) )
