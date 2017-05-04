class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = range(1,n+1)
        while len(res)>1:
        	res = zip(res, res[:len(res)//2-1:-1])
        return str(res[0]).replace(' ', '')


n = 8

sl = Solution()
print( sl.findContestMatch( n ) )