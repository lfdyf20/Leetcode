class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
        	return 0
        Asum = sum( A )
        maxVal = 0
        for i in range( len(A) ):
        	maxVal += i * A[i]
        resMax = maxVal
        for i in range(len(A)-1, 0, -1):
        	maxVal += Asum - A[i] * len(A)
        	resMax = max( resMax, maxVal )
        return resMax



A = [4, 3, 2, 6]

sl = Solution()
print( sl.maxRotateFunction( A ) )