# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

	def __str__(self):
		return "Interval[{}, {}]".format(self.start, self.end)


	def __repr__(self):
		return "Interval({}, {})".format(self.start, self.end)


import heapq
class SummaryRanges(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.intervals = []
	

	def addNum(self, val):
		"""
		:type val: int
		:rtype: void
		"""
		heapq.heappush( self.intervals, (val, Interval(val, val)) )
		

	def getIntervals(self):
		"""
		:rtype: List[Interval]
		"""
		stack = []
		while self.intervals:
			s, curr = heapq.heappop(self.intervals)
			if not stack:
				stack.append( curr )
			else:
				pre = stack[-1]
				if pre.end + 1 == curr.start:
					pre.end = max(pre.end, curr.end)
				else:
					stack.append( curr )
		self.intervals = stack
		return stack



# # Your SummaryRanges object will be instantiated and called as such:
# vals = [1,3,7,2,6]
# obj = SummaryRanges()
# for val in vals:
# 	obj.addNum(val)
# param_2 = obj.getIntervals()
# print(param_2)



# 	def __init__(self):
# 		self.intervals = []
		
# 	def addNum(self, val):
# 		heapq.heappush(self.intervals, (val, Interval(val, val)))

# 	def getIntervals(self):
# 		stack = []
# 		while self.intervals:
# 			idx, cur = heapq.heappop(self.intervals)
# 			if not stack:
# 				stack.append((idx, cur))
# 			else:
# 				_, prev = stack[-1]
# 				if prev.end + 1 >= cur.start:
# 					prev.end = max(prev.end, cur.end)
# 				else:
# 					stack.append((idx, cur))
# 		self.intervals = stack
# 		return list(map(lambda x: x[1], stack))



val = 

sl = Solution()
print( sl.addNum( val ) )