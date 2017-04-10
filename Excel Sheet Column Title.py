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
    
    def mySolution(self, n):
        res = ""
        while n>0:
            base = n%26
            if base == 0:
                res = 'Z' + res
                n = (n-1)//26
            else:
                res = chr(base+64) + res
                n = n//26
        return res

    def online(self, n):
        res = ""
        while n>0:
            n -= 1
            res = chr(n%26+65) + res
            n //= 26
        return res




n = 287979
sample = Solution()
print(sample.convertToTitle(n))
print( sample.mySolution(n) )
print( sample.online(n) )
