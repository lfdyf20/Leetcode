from tryFunc import timer

class Solution(object):
    
    def online_integerBreak(self, n):
    	"""
    	
    	from the leetcode discussion
    	
    	Arguments:
    		n {int} -- input
    		result {int} -- output
    	"""
    	if n == 2 or n == 3:
    		return n - 1
    	if n % 3 == 0:
    		return 3**(n//3)
    	if n % 3 == 1:
    		return 3**(n//3 - 1)*4
    	if n % 3 == 2:
    		return 3**(n//3)*2
    	"""
		From the hint:
		7 = 3 + 4 = 12
		8 = 3 + 3 + 2 = 18
		9 = 3 + 3 + 3 = 27
		10 = 3 + 3 + 4 = 36
		11 = 3 + 3 + 3 + 2 = 54
		12 = 3 + 3 + 3 + 3 = 81
		"""

    def dpSolution(self, n):
        dp = [0,0,1]
        for i in range(3,n+1):
            dp += [max(3*max(dp[i-3],i-3), 2*max(dp[i-2],i-2), 1*max(dp[i-1],i-1))]
        return dp[n]


    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
        	return 1
        if n == 2:
        	return 1
        elif n == 3:
        	return 2
        elif self.isOdd(n):
        	l, u = n/2-0.5, n/2+0.5
        	return int(max( l*u, self.integerBreak(l)*u, l*self.integerBreak(u) , self.integerBreak(l)*self.integerBreak(u)))
        else:
        	l, u = n/2-1 , n/2+1
        	m = n/2
        	return int(max( m*m, self.integerBreak(m)**2, l*u, self.integerBreak(l)*u, l*self.integerBreak(u) , self.integerBreak(l)*self.integerBreak(u) ))


    def isOdd(self, n):
    	"""
    	Arguments:
    		n {int} 
    		rtype {int}
    	"""
    	if n%2==1:
    		return True
    	else:
    		return False


    def ib(self, n):
        if n < 4:
            return n-1
        if n == 4:
            return 4
        res = 1
        while n > 4:
            res *= 3
            n = n - 3
        res *= n
        return res








n = 200
sample = Solution()
print( "online: ",sample.online_integerBreak(n) )
print( "integer break ",sample.integerBreak(n) )
print( "ib: ",sample.ib(n) )
print( "dp: ",sample.dpSolution(n) )