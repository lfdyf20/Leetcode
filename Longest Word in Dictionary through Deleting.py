class Solution(object):
    def findLongestWord(self, s, d):
    	# NOTE: iterator
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def inDict(s, word):
        	s = iter(s)
        	return all(i in s for i in word)

        return max( sorted([w for w in d if inDict(s, w)]) + [''], key=len )



s = "abpcplea"
d = ["ale","apple","monkey","plea"]
d = []

sl = Solution()
print( sl.findLongestWord( s, d ) )