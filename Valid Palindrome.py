import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = "".join( [ i.lower() for i in s if i.isalnum() ] )
        return new == new[::-1]
        # # 自学正则表达式
        # alpha = re.sub('[^A-Za-z]','',s)
        # alpha = alpha.lower()
        # print a
        # for i in range(len(alpha)/2):
        # 	if alpha[i]!= alpha[-1-i]:
        # 		return False

        # return True

    def isPalindromeOnline(self, s):
	    """
	    :type s: str
	    :rtype: bool
	    """
	    l = filter(lambda x: x.isalnum(), s.lower())
	    return l == l[::-1]


s = "12345"
sample = Solution()
print(sample.isPalindrome(s))
