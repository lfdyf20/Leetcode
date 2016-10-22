class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.sumM = []
        else:
            m, n = len(matrix), len(matrix[0])
            self.sumM = matrix[:]
            for i in range(m):
                for j in range(1,n):
                    self.sumM[i][j] = self.sumM[i][j-1] + matrix[i][j]
            for j in range(n):
                for i in range(1,m):
                    self.sumM[i][j] = self.sumM[i-1][j] + self.sumM[i][j]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.sumM:
            return 0
        res = self.sumM[row2][col2]
        if row1 > 0:
            res -= self.sumM[row1-1][col2]
        if col1 > 0:
            res -= self.sumM[row2][col1-1]
        if row1 > 0 and col1 > 0:
            res += self.sumM[row1-1][col1-1]
        return res



matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sl = NumMatrix(matrix)
print( sl.sumRegion(2, 1, 4, 3) )