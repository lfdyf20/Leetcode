class Solution(object):
	def countComponents(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: int
		"""
		visited = set()

		neigs = {}
		for p1, p2 in edges:
			neigs[p1] = neigs.get(p1, set()) | set([p2])
			neigs[p2] = neigs.get(p2, set()) | set([p1])
		
		count = 0

		for i in range(n):
			if i in visited:
				continue
			count += 1
			stack = [i]
			for curr in stack:
				if not curr in neigs:
					continue
				for to in neigs[curr]:
					stack.append(to)
					visited.add(to)
					neigs[to].discard(curr)
					if not neigs[to]:
						del neigs[to]
				del neigs[curr]
		return count


	def unionFind(self, n, edges):
		p = list(range(n))

		def find(v):
			if p[v] != v:
				p[v] = find(p[v])
			return p[v]

		for v, w in edges:
			p[find(v)] = find(w)
			print(p, v, w)
			
		return len(set(map(find, p)))






n = 5
edges = [[0,1],[1,2],[3,4]]

sl = Solution()
print( sl.countComponents( n, edges ) )
print( sl.unionFind(n, edges) )