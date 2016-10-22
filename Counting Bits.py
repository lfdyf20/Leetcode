class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(num+1):
        	i = bin( i )
        	result.append( i.count("1") )
        return result

         





num = 5
sample = Solution()
print( sample.countBits(num) )