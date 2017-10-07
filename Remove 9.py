class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = ''
        while n:
        	res = str( n%9 ) + res
        	n //= 9
        return res
        



n = 100

sl = Solution()
print( sl.newInteger( n ) )