class Solution(object):
	# BETTER: this is a much better way to code, I had thought
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
        	return 1
        ele = []
        while a > 1:
        	for d in range(9, 1, -1):
        		if a % d == 0:
        			a //= d
        			ele.append(d)
        			break
        	else:
        		return 0
        res = int("".join( map(str, ele[::-1]) ))
        return res if res < 2 ** 31 else 0
        



a = 48

sl = Solution()
print( sl.smallestFactorization( a ) )