class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """ 
        n = len(matrix)
        # if n==0:
        # 	return []
        res = [ [ 0 for _ in range(n)] for _ in range(n) ]
        for i in range(n):
        	for j in range(n):
        		# print(matrix[i][j], j, n-i-1)
        		res[j][n-i-1] = matrix[i][j]
        		# print(res)
        return res
        



matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
matrix = []

sl = Solution()
print( sl.rotate( matrix ) )