import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        m, n = len(grid), len(grid[0])
        dp = list( grid )
        for i in range(m):
        	for j in range(n):
        		if i==0 and j==0:
        			pass
        		elif i==0 and j>0:
        			dp[i][j] = dp[i][j-1]+grid[i][j]
        		elif i>=0 and j==0:
        			dp[i][j] = dp[i-1][j]+grid[i][j]
        		else:
        			dp[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return dp[-1][-1]

    def mp( self, grid ):
        m, n = len(grid), len(grid[0])
        rec = [[-1 for _ in range(n)] for _ in range(m) ] 
        rec[-1][-1] = grid[-1][-1]
        
        def travel( grid, i, j, m, n, rec ):
            y = np.array( rec )
            print(y)
            if rec[i][j] > 0:
                return rec[i][j]
            if i == m:
                rec[i][j] = sum( grid[i][j:] )
                return rec[i][j]
            if j == n:
                temp = [ row[j] for row in grid[i:] ]
                rec[i][j] = sum( temp )
                return rec[i][j]
            rec[i][j] = min( travel(grid,i+1,j,m,n,rec), travel(grid, i, j+1, m, n, rec) ) + grid[i][j]
            return rec[i][j]

        travel(grid, 0, 0, m-1, n-1, rec)
        return rec[0][0]

    def mySolution(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                if i == 0 and j == 0:
                    continue
                if i == 0 or j == 0:
                    grid[i][j] += [ grid[i-1][j], grid[i][j-1] ][ i==0 ]
                else:
                    grid[i][j] += min( grid[i-1][j], grid[i][j-1] )
        return grid[-1][-1]



grid = [[1,4,9],[3,5,8],[7,6,2],[3,1,4], [1,3,76]]
grid2 = [i[:] for i in grid]
sl = Solution()
print( sl.minPathSum(grid) )
print(grid)
print(grid2)
x = np.array( grid2 )
# print("x",x)
print( sl.mp(grid2) )