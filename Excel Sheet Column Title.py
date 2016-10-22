class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        base = ord('A')
        while n:
            n, r = divmod(n - 1, 26)
            res = '{}{}'.format(chr(base + r), res)
        return res

    def convertToTitle2(self, n):
        base = ord('A')
        n, r = divmod(n-1, 26)
        res = chr(base+r)
        print n, r, res
        return res



n = 28
sample = Solution()
print sample.convertToTitle(n)
print sample.convertToTitle2(n)