class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        index = [ (i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) ]
        index.sort( key=lambda x: (sum(x), -x[sum(x)%2]) )
        return [matrix[x][y] for (x,y) in index]






matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

sl = Solution()
print( sl.findDiagonalOrder( matrix ) )