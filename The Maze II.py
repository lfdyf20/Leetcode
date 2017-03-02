import numpy as np
import heapq
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if destination == start:
        	return True

        start = tuple(start)
        destination = tuple(destination)
        stack = [ (start,0) ]
        rec = set( start )
        dic = {tuple(start): 0}

        while stack:

        	(x,y), dis = stack.pop()
        	
        	nx, ny, d = x, y, dis
        	while nx>0 and maze[nx-1][ny]!=1:
        		nx -= 1
        		d += 1
        	if (nx,ny) not in rec or dic[(nx,ny)] > d:
        		rec.add( (nx,ny) )
        		stack.append( ([nx,ny],d) )
        		dic[(nx,ny)] = d
        	
        	nx, ny, d = x, y, dis
        	while nx<len(maze)-1 and maze[nx+1][ny]!=1:
        		nx += 1
        		d += 1
        	if (nx, ny) not in rec or dic[(nx,ny)] > d:
        		rec.add( (nx,ny) )
        		stack.append( ([nx,ny],d) )
        		dic[(nx,ny)] = d
        	
        	nx, ny, d = x, y, dis
        	while ny>0 and maze[nx][ny-1]!=1:
        		ny -= 1
        		d += 1
        	if (nx, ny) not in rec or dic[(nx,ny)] > d:
        		rec.add( (nx,ny) )
        		stack.append( ([nx,ny],d) )
        		dic[(nx,ny)] = d
        	
        	nx, ny, d = x, y, dis
        	while ny<len(maze[0])-1 and maze[nx][ny+1]!=1:
        		ny += 1
        		d += 1
        	if (nx, ny) not in rec or dic[(nx,ny)] > d:
        		rec.add( (nx,ny) )
        		stack.append( ([nx,ny],d) )
        		dic[(nx,ny)] = d

        return dic[tuple(destination)] if destination in dic else -1

    def online(self, maze, start, destination ):
    	dest = tuple( destination )
    	m, n = len(maze), len(maze[0])
    	res = None

    	def go( start, direction ):
    		x,y = start
    		i,j = direction
    		count = 0
    		while 0<=x+i<m and 0<=y+j<n and maze[x+i][y+j]!=1:
    			x, y = x+i, y+j
    			count += 1
    		return count, (x, y)

    	visited = {}
    	q = []
    	heapq.heappush(q, (0, tuple(start)))
    	while q:
    		length, cur = heapq.heappop(q)
    		if cur in visited and visited[cur]<=length:
    			continue
    		visited[ cur ] = length
    		if cur == dest:
    			res = min( res, length ) if res else length
    		for direction in [(-1, 0), (1, 0), (0,-1), (0,1)]:
    			nlength, pos = go(cur, direction)
    			heapq.heappush( q, (length+nlength, pos) )
    	return res if res else -1





maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]

sl = Solution()
print( sl.shortestDistance( maze, start, destination ) )
print( sl.online(maze, start, destination) )
