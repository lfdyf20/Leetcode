class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
        	return m*n
        minRow, minCol = m, n
        for row, col in ops:
        	minRow = min(minRow, row)
        	minCol = min(minCol, col)
        return minRow * minCol
        



m, n, ops = 3, 3, [] #[[[2,2],[3,3]]]

sl = Solution()
print( sl.maxCount( m, n, ops ) )