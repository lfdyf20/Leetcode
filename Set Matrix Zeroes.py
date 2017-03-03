import numpy as np
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """ 
        row = []
        vol = []
        for i in range(len(matrix)):
        	for j in range(len(matrix[0])):
        		if matrix[i][j] == 0:
        			row += [i]
        			vol += [j]
        for i in range(len(matrix)):
        	if i in row:
        		matrix[i] = [0] * len(matrix[i])
        	else:
        		for j in vol:
        			matrix[i][j] = 0
        return matrix

    def sz(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.deal( matrix, i, j )

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0


    def deal(self, matrix, i, j ):
        for colInd in range(len(matrix[i])):
            print(colInd)
            if matrix[i][colInd] != 0 and matrix[i][colInd] != '*':
                matrix[i][colInd] = '*'
        for rowInd in range(len(matrix)):
            if matrix[rowInd][j] != 0 and matrix[rowInd][j] != '*':
                matrix[rowInd][j] = '*'


    def mySolution(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                for j in range( len(matrix[0]) ):
                    matrix[i][j] = 0
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range( len(matrix) ):
                    matrix[i][j] = 0

        











matrix = [
	[1,2,3,4],
	[2,0,0,1],
	[3,4,5,1],
	[3,1,2,0]
]
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]

print(np.array(matrix))
# matrix = [[0]]
sl = Solution()
# print( sl.setZeroes( matrix ) )
# print(np.matrix(matrix))

# sl.sz(matrix)
# print(np.array(matrix))

sl.mySolution(matrix)
print(np.array(matrix))