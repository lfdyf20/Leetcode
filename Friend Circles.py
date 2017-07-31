class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = set()
        circle = 0

        def dfs(row):
        	visited.add(row)
        	for col in range(len(M[row])):
        		if M[row][col] and col not in visited:
        			dfs(col) 

        for row in range(len(M)):
        	if row not in visited:
        		dfs(row)
        		circle += 1
        return circle



M = [[1,1,0],
 [1,1,0],
 [0,0,1]]

sl = Solution()
print( sl.findCircleNum( M ) )