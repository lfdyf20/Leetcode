class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
        	r = (r + x/r)/2
        return r

    def mySqrt_BinaryTree(self, x):
    	l, r = 0, x
    	while l <= r:
    		m = (l+r)//2
    		if m*m <= x < (m+1)**2:
    			return m
    		elif m*m > x:
    			r = m-1
    		else:
    			l = m+1



x = 2147395599

sl = Solution()
print( sl.mySqrt_BinaryTree( x ) )