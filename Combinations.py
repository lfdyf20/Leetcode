class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """ 
        # return [ [i] + p
        #     for i in range(1, n+1)
        #     for p in self.combine( i-1, k-1) ] or [[]]
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]






n, k = 4, 2
sl = Solution()
print( sl.combine(n, k) )