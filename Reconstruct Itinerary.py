import collections
class Solution(object):
	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		ticketsDic = collections.defaultdict( set )
		itinerary = ['JFK']
		stack = ['JFK']
		for dep, arr in tickets:
			# print(dep, arr)
			ticketsDic[dep].add(arr)
		print(ticketsDic)
		res = []
		n = len(tickets)+1
		print(n)
		self.travel( ticketsDic, stack, ['JFK'], res, n )
		return res



	def travel(self, ticketsDic, stack, path, res, n):
		if len(path) == n:
			res.append( path )
			print(res)
			return
		if stack == []:
			if len(path) == n:
				res.append( path )
				return
			else:
				return
		# print("ticketsDic: ",ticketsDic)
		# print("stack: ",stack)
		# print("path:",path, len(path))
		# print("res: ", res)
		dep = stack.pop()
		if ticketsDic[ dep ] == set():
			return
		else:
			for arr in ticketsDic[ dep ]:
				print("arr: ", arr, ticketsDic[dep])
				tickets = ticketsDic.copy()
				tickets[ dep ].remove( arr )
				self.travel( tickets, stack + [arr], path + [arr], res, n )










tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

sl = Solution()
print( sl.findItinerary( tickets ) )