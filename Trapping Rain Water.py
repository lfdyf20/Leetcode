class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		def mdzz(height):
			pos, lmh = 0, height[0]
			res = 0
			for i in range(1, len(height)):
				if height[i] >= lmh:
					add = [lmh - h for h in height[pos+1:i]]
					res += sum(add)
					pos, lmh = i, height[i]
			return res

		def mdzzz(height):
			pos, lmh = 0, height[0]
			res = 0
			for i in range(1, len(height)):
				if height[i] > lmh:
					add = [lmh - h for h in height[pos+1:i]]
					res += sum(add)
					pos, lmh = i, height[i]
			return res

		# if height == height[::-1]:
		# 	return mdzz(height)
		if height == []:
			return 0

		res = mdzz( height ) + mdzzz(height[::-1])
		return res

				


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [3,1,4,1,5,9,2,6]
height = [1,0,1]
height = []

sl = Solution()
print( sl.trap( height ) )