class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.iterate_fibonacci(0,1,1)


    def iterate_fibonacci(self,a,b,i):
        if i>n:
            return b
        else:
            return self.iterate_fibonacci(b,a+b,i+1)

    def myCS( self, n ):
        if n < 3:
            return n
        l, r = 1, 2
        curr = 3
        while curr < n:
            l, r = r, l+r
            curr += 1
        return l + r


	
	




n = 11
sample = Solution()
print( sample.climbStairs(n) )
print( sample.myCS(n) )

