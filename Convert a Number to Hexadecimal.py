class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
        	return '0'
        if num < 0:
        	num += 2 ** 32
        d = '0123456789abcdef'
        res = ''
        while num:
        	res = d[num%16] + res
        	num = num//16       	
        return res
		        



num = -1

sl = Solution()
print( sl.toHex( num ) )