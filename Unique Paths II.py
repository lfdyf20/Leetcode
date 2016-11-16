import math
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0]*n]*m
        for i in range( m ):
        	for j in range( n ):
        		if obstacleGrid[i][j] != 0:
        			res[i][j] = 0
        			continue
        		if i==0 and j==0:
        			res[i][j] = 1
        		elif i==0:
        			res[i][j] = res[i][j-1]
        		elif j==0:
        			res[i][j] = res[i-1][j]
        		else:
        			res[i][j] = res[i][j-1] + res[i-1][j]
        return res[-1][-1]


    # def up(self, obstacleGrid):
    #     def count(m, n):
    #         return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))

    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     total = count(m, n)

    #     for i in range(m):
    #         for j in range(n):
    #             print(i,j)
    #             if obstacleGrid[i][j] != 0:
    #                 total -= count(m - i, n - j)
    #     return max(total, 0)



obstacleGrid = [
  [0,3,0],
  [0,1,0],
  [0,0,0]
]

obstacleGrid =[[0,0],[0,1]]

sl = Solution()
print( sl.uniquePathsWithObstacles( obstacleGrid ) )
# print( sl.up(obstacleGrid) )