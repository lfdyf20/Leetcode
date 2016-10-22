from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        sList = list(s)
        check = Counter(sList)
        for i in range(len(sList)):
        	if check[ sList[i] ] == 1:
        		return i







s = ""
sl = Solution()
print( sl.firstUniqChar(s) )