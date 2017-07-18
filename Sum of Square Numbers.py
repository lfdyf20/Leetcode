class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int((c//2)**0.5)+1):
        	if int((c-i**2)**0.5) == (c-i**2)**0.5:
        		return True
       	return False



c = 9

sl = Solution()
print( sl.judgeSquareSum( c ) )