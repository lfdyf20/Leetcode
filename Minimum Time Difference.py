class Solution(object):
	def findMinDifference(self, timePoints):
		"""
		:type timePoints: List[str]
		:rtype: int
		"""
		minutes = list(map(lambda s:int(s[:2])*60+int(s[-2:]), timePoints ))
		minutes.sort()
	
		return min( (y - x) % (24 * 60) for x, y in zip(minutes, minutes[1:] + minutes[:1]) )
		
	   



timePoints = ["23:59","00:00"]

sl = Solution()
print( sl.findMinDifference( timePoints ) )