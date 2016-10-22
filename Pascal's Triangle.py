class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(numRows-1):
            last = [0] + res[-1] + [0]
            path = []
            for i in range(len(last)-1):
                path.append( last[i]+last[i+1] )
            res.append(path)
        return res












numRows = 6
sample = Solution()
print(sample.generate(numRows))