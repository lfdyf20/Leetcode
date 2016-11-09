class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9,9,8,7,6,5,4,3,2,1]
        ans = 1
        product = 1
        for i in range( min(n, 10)):
        	product *= choices[i]
        	ans += product
        return ans


n = 4

sl = Solution()
print( sl.countNumbersWithUniqueDigits( n ) )