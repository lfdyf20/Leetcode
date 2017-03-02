import math
import time
# cache = {}
class Solution(object):
	cache = {}
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		""" 
		# global cache

		if n == 0:
			return 0
		if n < 0:
			return None
		if n in self.cache:
			return self.cache[n]
		else:
			answer = 1 + min( [self.numSquares(n-t*t) for t in range(1, int(math.sqrt(n))+1)] )
			self.cache[n] = answer
		return answer

	def bfs(self, n):
		record = [0]
		temp = []
		count = 0
		visited = [False] * (n+1)
		while True:
			count += 1
			for num in record:
				i = 0
				while True:
					i += 1
					sumVal = num + i*i
					if sumVal == n:
						return count
					if sumVal > n:
						break
					if visited[sumVal]:
						continue
					else:
						visited[sumVal] = True
					temp.append( sumVal )
			record = temp
			temp = []
		return 0

	

	










n = 383
sl = Solution()
start = time.time()
print( sl.numSquares(n) )
print( time.time()-start )


start = time.time()
print( sl.bfs(n) )
print( time.time()-start )