class Solution(object):
	def findRadius(self, houses, heaters):
		"""
		:type houses: List[int]
		:type heaters: List[int]
		:rtype: int
		"""
		heaters = sorted(heaters) + [float('inf')]
		i = r = 0
		for x in sorted(houses):
			while x >= sum(heaters[i:i+2]) / 2.:
				i += 1
			r = max(r, abs(heaters[i] - x))
		return r
		







houses, heaters = [1,1,1,1,1,1,999,999,999,999,999], [499,500,501]
sl = Solution()
print( sl.findRadius( houses, heaters ) )