class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0: 
            return 1
        elif n == 1:
            return 2
        elif n == 2:
            return 3 if m<2 else 4
        else:
            if m == 1:
                return 4
            elif m == 2:
                return 7
            else:
                return 8


n, m = 2, 3

sl = Solution()
print( sl.flipLights( n, m ) )