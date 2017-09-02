class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """ 
        res = []

       	def dfs(queens, xy_diff, xy_sum):
       		qlength = len(queens)
       		if qlength == n:
       			res.append( queens )
       			return

       		for q in range(n):
       			if q not in queens and qlength - q not in xy_diff and qlength + q not in xy_sum:
       				dfs(queens+[q], xy_diff + [qlength-q], xy_sum + [qlength+q])

       	dfs([], [], [])

       	return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res ]


n = 4

sl = Solution()
print( sl.solveNQueens(n) )