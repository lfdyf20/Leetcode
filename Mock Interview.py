import numpy as np
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0



matrix = [
    [1,2,0,1,2],
    [1,1,1,1,1],
    [1,0,1,1,1]
]

matrix = [[0]]

print(np.array(matrix))
sl = Solution()
sl.setZeroes( matrix )
print(np.array(matrix))