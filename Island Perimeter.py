class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        total = 0
        dup = 0
        for i in range(m):
        	for j in range(n):
        		if grid[i][j] == 1:
        			total += 1
        			for land in [ grid[x][y] for x,y in zip([i-1,i], [j,j-1]) if x>=0 and y>=0 ]:
        				if land == 1:
        					dup += 1
        res = 4*total - 2*dup
        return res




grid = [[0,1,0,0],
		 [1,1,1,0],
		 [0,1,0,0],
		 [1,1,0,0]]

sl = Solution()
print( sl.islandPerimeter( grid ) )