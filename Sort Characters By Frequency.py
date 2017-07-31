from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join([char * times for char, times in Counter(s).most_common()])
       

    def my(self, s):
    	return "".join(sorted(s, key=lambda x: (-s.count(x),x)))


s = "Aabb"
s = "loveleetcode"

sl = Solution()
print( sl.frequencySort( s ) )
print( sl.my(s) )