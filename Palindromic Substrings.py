class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        self.res = 0

        def findPal(i, j):
        	while i >= 0 and j<len(s) and s[i] == s[j]:
        		self.res += 1
        		i -= 1
        		j += 1

        for i in range(len(s)):
        	self.res += 1
        	findPal(i-1, i+1)
        	findPal(i-1, i)
        return self.res



s = "aabcb"

sl = Solution()
print( sl.countSubstrings( s ) )