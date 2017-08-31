import re
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        stack = []
        for pat in dict:
        	for match in re.finditer("(?={})".format(pat), s):
        		stack.append( [match.start(), match.start()+len(pat)] )
        stack.sort()
        mstack = []
        for i, (start, end) in enumerate(stack):
        	if i == 0 or start > mstack[-1][1]:
        		mstack.append( [start, end] )
        	else:
        		mstack[-1][1] = max(end, mstack[-1][1])
        for start, end in mstack[::-1]:
        	s = s[:start] + '<b>' + s[start:end] + '</b>' + s[end:]
        return s






s = "abcxyz123"
dict = ["abc","123"]

s = "aaabbcc"
s = ""
dict = ["aaa","aab","bc"]

sl = Solution()
print( sl.addBoldTag( s, dict ) )