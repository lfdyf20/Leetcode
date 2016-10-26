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


    def cb(self, num):
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        return res[:num+1]
        


         





num = 30
sample = Solution()
print( sample.countBits(num) )
print(sample.cb(num))