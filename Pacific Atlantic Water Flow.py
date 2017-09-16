class Solution(object):
	# REVIEW: clever
	def pacificAtlantic(self, matrix):
		def fill(ocean, stack):
			"""
	        :type matrix: List[List[int]]
	        :rtype: List[List[int]]
	        """
			while stack:
				r,c = stack.pop()
				if (r,c) in ocean: continue
				ocean.add((r,c))
				stack.extend([
					[nr, nc] for nr, nc in [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]
					if 0 <= nr < m and 0 <= nc < n and matrix[r][c] <= matrix[nr][nc]])
					
		if not matrix or not matrix[0]:	return []
		m, n = len(matrix), len(matrix[0])
		pacific, atlantic = set(), set()
		pstack = [[r,0] for r in range(m)] + [[0,c] for c in range(1,n)]
		astack = [[r,n-1] for r in range(m)] + [[m-1,c] for c in range(n-1)]

		fill(pacific, pstack)
		fill(atlantic, astack)
		
		return [list(x) for x in pacific&atlantic]



matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

sl = Solution()
print( sl.pacificAtlantic( matrix ) )