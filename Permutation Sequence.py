import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k-1
        nums = list(range(1, n+1))
        permutation = ''
        while n > 0:
        	n -= 1
        	fac = math.factorial( n )
        	# index, k = divmod(k, math.factorial(n))
        	index, k = k//fac, k%fac
        	permutation += str(nums[index])
        	nums.remove( nums[index] )
       	return permutation 




n, k = 3, 5

sl = Solution()
print( sl.getPermutation( n, k ) )