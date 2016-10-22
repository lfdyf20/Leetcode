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


        # if len(grid) == 1:
        # 	return sum( grid[0] )
        # isCol = True

        # sumVal = 0
        # for i in grid:
        # 	sumVal += i[0]
        # 	if len(i) != 1:
        # 		isCol = False
        # if isCol == True:
        # 	return sumVal
       

        # orgin = grid[0][0]
        # g1 = grid[1:]
        # g2 = list( map(lambda x:x[1:], grid))
        # gridSum = orgin + min( self.minPathSum(g1), self.minPathSum(g2) )



grid = [[1,4,9],[3,5,8],[7,6,2]]
sl = Solution()
print( sl.minPathSum(grid) )