import numpy as np
from DecoratorHelper import timer

class Solution(object):
	@timer
	def updateMatrix(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		if not matrix or not matrix[0]:
			return matrix
		m, n = len(matrix), len(matrix[0])
		res = [ [0]*n for _ in range(m) ]
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 1:
					res[i][j] = float('inf')
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					stack = [ [ii,jj] for ii, jj in [ (i+1,j),(i-1,j),(i,j-1),(i,j+1) ]
							if 0<=ii<m and 0<=jj<n and matrix[ii][jj]==1 ]
					visited = set()
					dis = 1
					while stack:
						temp = []
						for x, y in stack:
							if res[x][y] <= dis:
								continue
							else:
								res[x][y] = dis
							visited.add((x,y))
							temp += [ [ii,jj] for ii, jj in [ (x+1,y),(x-1,y),(x,y-1),(x,y+1) ]
										if 0<=ii<m and 0<=jj<n and matrix[ii][jj]==1 and (ii,jj) not in visited ]
						stack, dis = temp, dis + 1
		return res

	@timer
	def another(self, matrix):
		visited = set()
		queue = []
		m, n = len(matrix), len(matrix[0])
		res = [ [0]*n for _ in range(m) ]
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					queue += [ (ii,jj) for ii, jj in [(i+1,j), (i-1,j), (i,j+1), (i, j-1)] 
								if 0 <=ii<m and 0<=jj<n and matrix[ii][jj] not in visited and matrix[ii][jj]==1 ]
		dis = 1
		while queue:
			temp = []
			for i, j in queue:
				if (i, j) in visited:
					continue
				res[i][j] = dis
				visited.add((i,j))
				temp += [ (ii,jj) for ii, jj in [(i+1,j), (i-1,j), (i,j+1), (i, j-1)] 
								if 0 <=ii<m and 0<=jj<n and matrix[ii][jj] not in visited and matrix[ii][jj]==1 ]
			dis += 1
			queue = temp
		return res



matrix = [[0,1,0],[1,1,1],[1,1,1]]
# matrix = []

sl = Solution()
print( sl.updateMatrix( matrix ) )
print( sl.another(matrix) )