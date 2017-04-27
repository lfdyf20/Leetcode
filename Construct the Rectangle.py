class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        ub = int(area**0.5)
        for i in range(ub, 0, -1):
        	if area%i == 0:
        		return sorted([i, area//i], reverse=True)
        



area = 8

sl = Solution()
print( sl.constructRectangle( area ) )