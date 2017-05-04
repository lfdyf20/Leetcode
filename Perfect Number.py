class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 :
        	return False

        ub = int(num**0.5)

        res = sum( i + num//i for i in range(1,ub+1) if not num%i )

        if ub**2 == num:
        	num -= ub

        return num == res - num
        



num = 28

sl = Solution()
print( sl.checkPerfectNumber( num ) )