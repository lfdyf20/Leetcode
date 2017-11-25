class Solution(object):
    def validPalindrome(self, s, flag = 1):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l < r:
        	if s[l] == s[r]:
        		l += 1
        		r -= 1
        	elif flag == 0:
        		return False
        	else:
        		return self.validPalindrome(s[l+1:r+1], 0) or self.validPalindrome(s[l:r], 0)
        return True


        



s = "aba"
s = "abca"
s = "abbca"
s = "abbbcda"
s = ""
s = "acbca"

sl = Solution()
print( sl.validPalindrome( s ) )