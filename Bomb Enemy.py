class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0 
        for i in range( len(grid) ):
        	for j in range( len(grid[0]) ):
        		if grid[i][j] == '0':
        			# print(i,j)
        			x, y = i, j
        			count = 0
        			i, j = x, y
        			while i > 0 and grid[i][j] != 'W':
        				i -= 1
        				if grid[i][j] == "E":
        					# print("up")
        					count += 1
        			i, j = x, y
        			while i < len(grid)-1 and grid[i][j] != 'W':
        				i += 1
        				if grid[i][j] == "E":
        					# print("down")
        					count += 1
        			i, j = x, y
        			while j > 0 and grid[i][j] != "W":
        				j -= 1
        				if grid[i][j] == "E":
        					# print("left", i,j)
        					count += 1
        			i, j = x, y
        			while j < len(grid[0])-1 and grid[i][j] != 'W':
        				j += 1
        				if grid[i][j] == "E":
        					# print("right", i,j)
        					count += 1
        			res = max(res, count)
        return res

    def mySolution(self, grid):
    	if not grid or not grid[0]:
    		return 0
    	rowLen, colLen = len(grid), len(grid[0])
    	
    	self.grid = grid
    	self.value = [[0]*colLen for _ in range( rowLen )]

    	for i in range( rowLen ):
    		count = 0
    		for j in range( colLen ):
    			if grid[i][j] == '0': self.value[i][j] += count
    			if grid[i][j] == 'E': count += 1
    			if grid[i][j] == 'W': count = 0
    		count = 0
    		for j in reversed( range(colLen) ):
    			if grid[i][j] == '0': self.value[i][j] += count
    			if grid[i][j] == 'E': count += 1
    			if grid[i][j] == 'W': count = 0

    	for j in range(colLen):
    		count = 0
    		for i in range( rowLen ):
    			if grid[i][j] == '0': self.value[i][j] += count
    			if grid[i][j] == 'E': count += 1
    			if grid[i][j] == 'W': count = 0
    		count = 0
    		for i in reversed( range( rowLen ) ):
    			if grid[i][j] == '0': self.value[i][j] += count
    			if grid[i][j] == 'E': count += 1
    			if grid[i][j] == 'W': count = 0

    	return max([max(v) for v in self.value])





# grid = [
# ['0', 'E', '0', '0'],
# ['E', '0', 'W', 'E'],
# ['0', 'E', '0', '0']
# ]

grid = ["0E00","E0WE","0E00"]

# grid = ["0E0W"]

sl = Solution()
print( sl.maxKilledEnemies( grid ) )