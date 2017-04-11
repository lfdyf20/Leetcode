import numpy as np
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtypen: int
        """
        m = len(matrix)
        n = len(matrix[0])
        record = [ [0 for _ in range(n)] for _ in range(m) ]
        maxVal = 0
        # print(record)
        for j in range(n):
        	record[0][j] = int( matrix[0][j] )
        	maxVal = max( maxVal, record[0][j] )
        for i in range(m):
        	record[i][0] = int( matrix[i][0] )
        	maxVal = max( maxVal, record[i][0] )
        for i in range(1,m):
        	for j in range(1,n):
        		if matrix[i][j] == '1':
	        		record[i][j] = min( record[i-1][j-1], record[i-1][j], record[i][j-1] )+1
	        		maxVal = max( maxVal, record[i][j] )
        print(record)
        return maxVal * maxVal

    def mySolution(self, matrix):
        # record = [ [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ]
        record = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        if sum(record[0])>0 or sum(list(zip(*record))[0])>0:
            res = 1
        else:
            res = 0
        for i in range( 1,len(record) ):
            for j in range( 1,len(record[i]) ):
                if record[i][j]==1:
                    # record[i][j] = max(record[i][j], 
                    #                 min(record[i-1][j-1], record[i-1][j], record[i][j-1])+1 )
                    record[i][j] = min(record[i-1][j-1], record[i-1][j], record[i][j-1])+1
                    res = max( res, record[i][j] )
        return res**2

    def online(self, matrix):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i and j:
                    A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
        return len(A) and max(map(max, A)) ** 2




matrix = [
	[1,0,1,0,0],
	[1,0,1,1,1],
	[1,1,1,1,1],
	[1,0,0,1,0]
]

matrix = [[1]]

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		matrix[i][j] = str(matrix[i][j])
print(matrix) 


sl = Solution()
print( sl.maximalSquare( matrix ) )
print( sl.mySolution(matrix) )