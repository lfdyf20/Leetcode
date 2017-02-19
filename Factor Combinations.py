class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n <= 1:
            return []
        
        res = []
        
        i = 2
        while i * i <= n:
            if n % i == 0:
                q = n // i
                res.append([i, q])
                subres = self.getFactors(q)
                for r in subres:
                    # if r[0] >= i:
                    res.append([i] + r)
            i += 1
                
        return res



n = 24

sl = Solution()
print( sl.getFactors( n ) )