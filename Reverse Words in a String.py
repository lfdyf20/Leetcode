import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip(" ")
        s = re.sub( " +"," ",s )
        wordList = s.split(" ")
        return " ".join( wordList[::-1] )
        



s = "      the sky     is blue  "

sl = Solution()
print( sl.reverseWords( s ) )