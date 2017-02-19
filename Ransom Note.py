from collections import Counter
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


    def mySolution(self, ransomNote, magazine):
        m = Counter(magazine)
        r = Counter(ransomNote)
        for i in r:
            if r[i] > m[i]:
                return False
        return True

    def online(self, ransomNote, magazine):
        print(Counter(ransomNote) - Counter(magazine))
        return not Counter(ransomNote) - Counter(magazine)





ransomNote = 'aabc'
magazine = 'aab'
sl = Solution()
print( sl.canConstruct(ransomNote, magazine) )
print( sl.mySolution(ransomNote, magazine) )
print( sl.online(ransomNote, magazine) )