import numpy as np
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if destination == start:
        	return True

        start = tuple(start)
        destination = tuple(destination)
        stack = [ start ]
        print(stack)
        rec = set( [start] )

        while stack:
        	x,y = stack.pop()
        	
        	nx, ny = x, y
        	while nx>0 and maze[nx-1][ny]!=1:
        		nx -= 1
        	if (nx,ny) not in rec:
        		rec.add( (nx,ny) )
        		stack.append( (nx,ny) )
        	
        	nx, ny = x, y
        	while nx<len(maze)-1 and maze[nx+1][ny]!=1:
        		nx += 1
        	if (nx, ny) not in rec:
        		rec.add( (nx,ny) )
        		stack.append( (nx,ny) )
        	
        	nx, ny = x, y
        	while ny>0 and maze[nx][ny-1]!=1:
        		ny -= 1
        	if (nx, ny) not in rec:
        		rec.add( (nx,ny) )
        		stack.append( (nx,ny) )
        	
        	nx, ny = x, y
        	while ny<len(maze[0])-1 and maze[nx][ny+1]!=1:
        		ny += 1
        	if (nx, ny) not in rec:
        		rec.add( (nx,ny) )
        		stack.append( (nx,ny) )

        	if destination in rec:
        		return True

        print(rec)
        return False




maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]

sl = Solution()
print( sl.hasPath( maze, start, destination ) )

print(np.array(maze))