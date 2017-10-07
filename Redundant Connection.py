class Union(object):
	def __init__(self):
		self.union = {}

	def find(self, node):
		if node not in self.union:
			self.union[ node ] = node
		while self.union[ node ] != node:
			node = self.union[ node ]
		return node



class Solution(object):
	def findRedundantConnection(self, edges):
		"""
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		thisUnion = Union()
		for a, b in edges:
			if thisUnion.find(a) == thisUnion.find(b):
				return [a,b]
			else:
				thisUnion.union[ thisUnion.find(b) ] = thisUnion.find(a)



edges = [[1,2], [1,3], [2,3]]
edges = [[1,3],[3,4],[1,5],[3,5],[2,3]]

sl = Solution()
print( sl.findRedundantConnection( edges ) )




class Union(object):
	def __init__(self):
		self.union = {}
		
	def find(self, node):
		if node not in self.union:
			self.union[node] = node
		while self.union[node] != node:
			node = self.union[node]