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
    		return 3**(n/3)
    	if n % 3 == 1:
    		return 3**(n/3 - 1)*4
    	if n % 3 == 2:
    		return 3**(n/3)*2
    	"""
		From the hint:
		7 = 3 + 4 = 12
		8 = 3 + 3 + 2 = 18
		9 = 3 + 3 + 3 = 27
		10 = 3 + 3 + 4 = 36
		11 = 3 + 3 + 3 + 2 = 54
		12 = 3 + 3 + 3 + 3 = 81
		"""





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








n = 10
sample = Solution()
print( sample.online_integerBreak(n) )
# print(7%2)