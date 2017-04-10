class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dic = {}
        maxEdges = 0
        for i in range(len(wall)):
        	width = 0
        	for j in range(len(wall[i])-1):
        		width += wall[i][j]
        		dic[ width ] = dic.get(width, 0)+1
        		maxEdges = max( maxEdges, dic[ width ] )
        return len(wall) - maxEdges



wall = [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]

sl = Solution()
print( sl.leastBricks( wall ) )