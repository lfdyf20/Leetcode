from tryFunc import timer
class Solution(object):
	@timer
	def findLonelyPixel(self, picture):
		"""
		:type picture: List[List[str]]
		:rtype: int
		"""
		index = set(range(len(picture[0])))
		colsHistory = set()
		res = set()
		for i in range(len(picture)):
			toRemove = set()
			toAdd = set()
			for j in index:
				if picture[i][j] == 'B':
					if j in colsHistory:
						toRemove.add(j)
						res.discard(j)
					else:
						toAdd.add(j)
			colsHistory |= toAdd
			if len(toAdd) == 1 and len(toRemove) == 0:
				res |= toAdd
			index = index - toRemove
		# 	print(i, picture[i], res)
		
		# print(res)
		
		return len(res)

	@timer
	def oneliner(self, picture):
		return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))

			


		



picture = [['W', 'W', 'B'],
		   ['W', 'B', 'W'],
		   ['B', 'W', 'W']]
# picture = ['B','B', 'B']
picture = [ "BWWWBBBBWW",
			"WWBWBBBWBB",
			"WWBWWWWWBW",
			"BBWWWWWBWW",
			"BBWWWBBBWW",
			"BBBWWWBBBW",
			"BBBBWWWWBB",
			"WWBWWBWWBB",
			"WBBWWWWWWW",
			"BWBWWBBBBW"]

sl = Solution()
print( sl.findLonelyPixel( picture ) )
print( sl.oneliner(picture) )