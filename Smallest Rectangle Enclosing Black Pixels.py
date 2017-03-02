class Solution(object):
	def minArea(self, image, x, y):
		"""
		:type image: List[List[str]]
		:type x: int
		:type y: int
		:rtype: int
		"""
		m, n = len(image), len(image[0])
		stack = [ (x,y) ]
		ml = mu = float("inf")
		mr = md = float("-inf")

		visited = set()
		while stack:
			r, c = stack.pop()
			visited.add( (r,c) )
			ml, mr = min(ml, c), max(mr, c)
			mu, md = min(mu, r), max(md, r)
			for i,j in [(r-1,c),(r+1,c),(r,c+1), (r,c-1)]:
				if 0<=i<m and 0<=j<n and image[i][j] == '1' and (i,j) not in visited:
					stack.append( (i,j) )

		return (mr-ml+1)*(md-mu+1)

	def online(self, image, x, y):
		def first(lo, hi, check):
			while lo < hi:
				mid = (lo + hi) // 2
				if check(mid):
					hi = mid
				else:
					lo = mid + 1
			return lo
		top    = first(0, x,             lambda x: '1' in image[x])
		bottom = first(x, len(image),    lambda x: '1' not in image[x])
		left   = first(0, y,             lambda y: any(row[y] == '1' for row in image))
		right  = first(y, len(image[0]), lambda y: all(row[y] == '0' for row in image))
		return (bottom - top) * (right - left)






image = [
  "0010",
  "0110",
  "0100"
]
x, y = 0, 2


sl = Solution()
print( sl.minArea( image, x, y ) )
print( sl.online(image, x, y) )