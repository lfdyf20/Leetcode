import numpy as np
class Solution(object):
	def canCross(self, stones):
		"""
		:type stones: List[int]
		:rtype: bool
		""" 
		if stones[0] != 0 or stones[1] != 1:
			return False

		dp = [[False]*(stones[-1]+1) for _ in range(stones[-1]+1)]

		dp[0][0] = dp[1][1] = True

		for i in range(2, stones[-1]+1):
			for j in range(stones[-1]+1):
				if i not in stones or i-j not in stones:
					continue
				dp[i][j] = any(dp[i-j][k] for k in [j-1,j,j+1] if k>=0 and k<=stones[-1])
					
		return any(dp[-1])

	def another(self, stones):
		if stones[0] != 0 or stones[1] != 1:
			return False
		dic = {stone:set() for stone in stones}
		dic[0].add(0)
		dic[1].add(1)
		for stone in stones[1:]:
			for pace in dic[stone]:
				for p in [pace-1, pace, pace+1]:
					s = stone + p
					if p > 0 and s in dic:
						dic[s].add(p)
		return len(dic[stones[-1]])!=0


	def online(self, stones):
		stones_set, fail = set(stones), set()
		stack = [(0,0)]
		while stack:
			stone, pace = stack.pop()
			for p in [pace-1, pace, pace+1]:
				s = stone + p
				if p > 0 and s in stones_set and (s, p) not in fail:
					if s == stones[-1]:
						return True
					stack.append( (s, p) )
			fail.add( (stone, pace) )
		return False









stones = [0,1,3,5,6,8,12,17]
# stones = [0,1]
# stones = [0,1,2,3,4,8,9,11]
stones = [0, 2]


sl = Solution()
print( sl.canCross( stones ) )
print( sl.another( stones ) )