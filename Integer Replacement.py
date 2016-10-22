class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
        	return 0
        if n%2 == 0:
        	return self.integerReplacement(int(n/2))+1
        else:
        	return min(self.integerReplacement(int(n+1)), self.integerReplacement(int(n-1)))+1
     	   



n = 7

sl = Solution()
print( sl.integerReplacement( n ) )