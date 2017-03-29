class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if not board:
			return False
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.trave(board, i, j, word):
					return True
		return False

	def trave(self, board, i, j, word):
		if word == "":
			return True
		if i<0 or i>=len(board) or j<0 or j>=len(board[0]) \
			 or word[0] != board[i][j]:
			return False
		temp = board[i][j]
		board[i][j] = '#'
		res = self.trave(board, i+1, j, word[1:]) or \
				self.trave(board, i-1, j, word[1:]) or \
				self.trave(board, i, j+1, word[1:]) or \
				self.trave(board, i, j-1, word[1:])
		board[i][j] = temp
		return res





board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

sl = Solution()
print( sl.exist( board, word ) )