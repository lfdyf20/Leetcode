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




matrix = [
	[1,0,1,0,0],
	[1,0,1,1,1],
	[1,1,1,1,1],
	[1,0,0,1,0]
]

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		matrix[i][j] = str(matrix[i][j])
print(matrix) 


sl = Solution()
print( sl.maximalSquare( matrix ) )