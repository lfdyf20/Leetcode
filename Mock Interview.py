mat = [
	[".","S","#",".",".","E"],
	[".","#",".","0",".","."],
	[".",".",".",".",".","."]
	]

def isNear(x1, y1, x2, y2):
	if x2 == x1-1 and y1 == y2:
		return "D"
	if x2 == x1+1 and y1 == y2:
		return "U"
	if x1 == x2 and y1-1 == y2:
		return "L"
	if x1 == x2 and y1+1 == y2:
		return "R"
	return "N"

def bfs(mat):
	m, n = len(mat), len(mat[0])
	queue, visited = [], set()
	dp = {}
	for i in range(m):
		for j in range(n):
			if mat[i][j] == "0":
				bi, bj = i, j
			if mat[i][j] == "E":
				pi, pj = i, j
			if mat[i][j] == "S":
				ti, tj = i, j
	dp[bi,bj,pi,pj] = 1
	queue = [(bi,bj,pi,pj)]
	for i, j, ii, jj in queue:
		r = isNear(i, j, ii, jj)
		if r == "N":
			toExpand = [i+]

	print(dp)


bfs(mat)