import itertools
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m == 0 and n ==0:
        	return
        for iM in range(m):
        	for iN in range(n):
        		count = sum( [board[i][j]%2 for i in range(iM-1, iM+2) for j in range(iN-1,iN+2) if 0<=i<m and 0<=j<n ]) - board[iM][iN]
        		if board[iM][iN] == 0 and count == 3:
        			board[iM][iN] = 2
        		if board[iM][iN] == 1 and ( count < 2 or count > 3 ):
        			board[iM][iN] = 3
        for i in range(m):
        	for j in range(n):
        		if board[i][j] == 2:
        			board[i][j] = 1
        		if board[i][j] == 3:
        			board[i][j] = 0






board = [
	[1,1,0,1],
	[0,1,1,0],
	[0,1,0,1],
]

sl = Solution()
sl.gameOfLife( board )
print(board)

