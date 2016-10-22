from math import floor
class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		""" 
		if matrix:
			row,col,width=len(matrix)-1,0,len(matrix[0])
			while row>=0 and col<width:
				if matrix[row][col]==target:
					return True
				elif matrix[row][col]>target:
					row=row-1
				else:
					col=col+1
			return False



		





target = 14

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


sl = Solution()
print(sl.searchMatrix(matrix, target))

