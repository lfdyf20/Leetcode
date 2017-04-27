class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([ word[::-1] for word in s.split() ])
        


s = "Let's take LeetCode contest"

sl = Solution()
print( sl.reverseWords( s ) )