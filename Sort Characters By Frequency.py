from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join([char * times for char, times in Counter(s).most_common()])
       




s = "Aabb"

sl = Solution()
print( sl.frequencySort( s ) )