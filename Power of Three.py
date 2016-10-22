class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
        	return False
        elif n == 1:
        	return True
        elif n % 3 == 0:
        	return self.isPowerOfThree(n/3)
        else:
        	return False




n = [0,1,6,100,3,9]
sample = Solution()
for i in n:
	print i
	print sample.isPowerOfThree(i)