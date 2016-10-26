class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        rec = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = ''
        while n > 26:
            rem = n % 26
            res = rec[rem-1] + res
            n = (n-1) // 26
        res = rec[n-1] + res
        return res
    #     res = ''
    #     base = ord('A')
    #     while n:
    #         n, r = divmod(n - 1, 26)
    #         res = '{}{}'.format(chr(base + r), res)
    #     return res

    # def convertToTitle2(self, n):
    #     base = ord('A')
    #     n, r = divmod(n-1, 26)
    #     res = chr(base+r)
    #     print n, r, res
    #     return res



n = 28
sample = Solution()
print(sample.convertToTitle(n))
# print sample.convertToTitle2(n)