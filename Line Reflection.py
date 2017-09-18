class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
        	return True
        sumVal = max(points)[0] + min(points)[0]
        return { (x,y) for x,y in points} == { (sumVal-x, y) for x,y in points }



points = [[1,1],[-1,1]]

sl = Solution()
print( sl.isReflected( points ) )