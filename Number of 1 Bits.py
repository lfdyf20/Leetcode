class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        print bin(n)
        return bin(n).count('1')
        


n = 0
sample = Solution()
print sample.hammingWeight(n)