class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
        	return 0
        rec = [(0,0,0,0) for _ in range(len(M[0]) + 2)]
        res = 0
        for i in range(1, len(M)+1):
        	curr = [(0,0,0,0)]
        	for j in range(1, len(M[0])+1):
        		if M[i-1][j-1] == 1:
        			up, left, diag, adiag = rec[j][0], curr[-1][1], rec[j-1][2], rec[j+1][3]
        			up, left, diag, adiag = up + 1, left + 1, diag + 1, adiag + 1
        			this = (up, left, diag, adiag)
        			res = max( *this, res )
        			print(this)
        			curr.append( this )
        		else:
        			curr.append( (0,0,0,0) )
        	curr.append( (0,0,0,0) )
        	rec = curr
        	print("")
        return res



M = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
M = [[]]
M = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]

sl = Solution()
print( sl.longestLine( M ) )