class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """ 
        dict = {}
        for i in list( magazine ):
        	if i in dict:
        		dict[i] += 1
        	else:
        		dict[i] = 1
        for i in list( ransomNote ):
        	if i in dict:
        		dict[i] -= 1
        		if dict[i] < 0:
        			return False
        	else:
        		return False
        return True







ransomNote = 'aa'
magazine = 'ab'
sl = Solution()
print( sl.canConstruct(ransomNote, magazine) )