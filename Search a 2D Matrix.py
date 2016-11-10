class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		for i in range(len(matrix)):
			if matrix[i][0] > target:
				for j in range( len(matrix[0]) ):
					if matrix[i-1][j] == target:
						return True
				return False
		for j in range(len(matrix[0])):
			if matrix[-1][j] == target:
				return True
		return False




matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 34
sl = Solution()
print( sl.searchMatrix( matrix, target ) )
