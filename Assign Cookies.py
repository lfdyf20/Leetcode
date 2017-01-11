class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort( reverse = True)
        count = 0
        for child in g:
        	while s and s[-1] < child:
        		s.pop()
        	if not s:
        		return count
        	s.pop()
        	count += 1
        return count



g, s = [1], [1]

sl = Solution()
print( sl.findContentChildren( g, s ) )