class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """ 
        res = [1]
        row = 0
        while row < rowIndex:
        	res = [i+j for i,j in zip([0]+res, res+[0])]
        	row += 1
        return res





rowIndex = 0

sl = Solution()
print( sl.getRow(rowIndex) )