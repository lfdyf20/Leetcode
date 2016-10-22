class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        re=[0]
        for i in range(n):
        	print(i)
        	re=re+[2**i+x for x in re[::-1]]
        	print(re)
        return re




n = 3
sl = Solution()
print( sl.grayCode(n) )

