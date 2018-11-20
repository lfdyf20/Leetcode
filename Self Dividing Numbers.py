class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
        	snum = str( num )
        	if '0' in snum:
        		continue
        	if all( map( lambda x:num % int(x) == 0, snum ) ):
        		res.append( num )
        return res
        



left, right = 1, 22
left, right = 1, 1

sl = Solution()
print( sl.selfDividingNumbers( left, right ) )