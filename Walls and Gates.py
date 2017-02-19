class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        gates = [(i,j) for i,row in enumerate(rooms) for j,room in enumerate(row) if not room]
        for i, j in gates:
            for x, y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<len(rooms) and 0<=y<len(rooms[0]) and rooms[x][y]>2**30:
                    rooms[x][y] = rooms[i][j] + 1
                    gates += (x, y),
                    


INF = 2**30+1

rooms = [
[INF,  -1,  0,  INF],
[INF, INF, INF,  -1],
[INF,  -1, INF,  -1],
[  0,  -1, INF, INF],
]

sl = Solution()
print( sl.wallsAndGates( rooms ) )