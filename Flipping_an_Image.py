class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [ [1-i for i in reversed(row)] for row in A ]



A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

sl = Solution()
print( sl.flipAndInvertImage( A ) )