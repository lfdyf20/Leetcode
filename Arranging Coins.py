class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n//2+1

        while l <= r:
        	mid = (l+r)//2
        	midVal = mid*(mid+1)//2

        	if midVal == n:
        		return mid
        	elif midVal < n:
        		l = mid + 1
        	else:
        		r = mid - 1
        return l-1 #if n>1 else 1



n = 1

sl = Solution()
print( sl.arrangeCoins( n ) )