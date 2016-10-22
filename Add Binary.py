class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """ 
        x = int(a, 2)
        y = int(b, 2)
        return (bin(x+y))[2:]
        




a = '1'
b = '11'
sl = Solution()
print( sl.addBinary( a,b ) )