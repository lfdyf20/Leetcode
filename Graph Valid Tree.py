class Solution(object):
	def validTree(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: bool
		""" 
		dic = {i:set() for i in range(n)}
		for i, j in edges:
			dic[i].add(j)
			dic[j].add(i)
		stack = [ dic.keys()[0] ]
		visited = set()
		while stack:
			node = stack.pop()
			if node in visited:
				return False
			visited.add( node )
			for neighbour in dic[node]:
				stack.append( neighbour )
				dic[neighbour].remove(node)
			dic.pop(node)
		return not dic

		



n, edges = 5, [[0, 1], [3,4]]
n, edges = 1, []

sl = Solution()
print( sl.validTree( n, edges ) )