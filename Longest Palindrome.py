from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter( s )
        res, flag = 0, 0
        for num, c in counter.items():
        	if c%2 == 0:
        		res += c
        	else:
        		flag = 1
        		res += c-1
        return res+flag



s = "abccccdd"

sl = Solution()
print( sl.longestPalindrome( s ) )