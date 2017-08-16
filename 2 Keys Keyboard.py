class Solution(object):
	# FAVE: clever
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n+1):
        	while n % i == 0:
        		res += i
        		n = n //i
        return res
        



n = 9
n = 25
n = 27

sl = Solution()
print( sl.minSteps( n ) )