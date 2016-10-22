class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	x = -x
        xList = list( str(x) )
        xList.reverse()
        reverse = ''.join(xList)
        xReverse = int(reverse)
        if xReverse == x:
        	return True
        else:
        	return False



x = -2147447412
sample = Solution()
print sample.isPalindrome(x)
