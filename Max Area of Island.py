class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		if grid[i][j] == 1:
        			stack = [(i,j)]
        			grid[i][j] = 0
        			count = 1
        			for x, y in stack:
        				for xx, yy in [(x+1, y),(x-1,y),(x,y+1),(x,y-1)]:
        					if 0<=xx<len(grid) and 0<=yy<len(grid[0]) and grid[xx][yy] == 1:
        						stack.append((xx, yy))
        						grid[xx][yy] = 0
        						count += 1
        			res = max(res, count)
        return res
        					



grid = [
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# grid = [[0,0,0,0,0,0,0,0]]
# grid = [[1]]
sl = Solution()
print( sl.maxAreaOfIsland( grid ) )