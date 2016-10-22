import numpy as np
class Solution(object):
	def numIslands(self, grid):
	    """
	    :type grid: List[List[str]]
	    :rtype: int
	    """
	    if not grid:
	        return 0
	        
	    m = len(grid)
	    n = len(grid[0])
	    sum  = 0
	    
	    for i in range(m):
	        for j in range(n):
	            
	            if grid[i][j] == "0":
	                continue
	            else:
	                
	                #sum up only once per chance of meeting "1"
	                sum += 1
	                stack = list()
	                stack.append([i,j])
	                
	                #visit each "1" in the adjacent area using a stack
	                while len(stack) != 0:
	                    
	                    [p,q] = stack.pop()
	                    
	                    if p >= 1 and grid[p-1][q] == "1":
	                        stack.append([p-1,q])
	                        
	                    if p < m -1 and grid[p+1][q] == "1":
	                        stack.append([p+1,q])
	                    
	                    if q >= 1 and grid[p][q-1] == "1":
	                        stack.append([p,q-1])
	                        
	                    if q < n - 1 and grid[p][q + 1] == "1":
	                        stack.append([p,q+1])
	                    
	                    #mark as visited
	                    grid[p][q] = "0"
	    
	    
	    
	    return sum

		
			




		# print(np.matrix(newGrid))


grid = [
	[1,1,1,0,0],
	[1,1,0,0,0],
	[0,1,0,0,0],
	[0,0,1,0,0],
	[0,0,0,0,1],
	[0,0,0,1,1]
]

sl = Solution()
print( sl.numIslands( grid ) )