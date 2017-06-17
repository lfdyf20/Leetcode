# coding: utf-8
import numpy as np
class Solution(object):
	def calculateMinimumHP(self, dungeon):
		"""
		:type dungeon: List[List[int]]
		:rtype: int
		"""
		row, col = len(dungeon), len(dungeon[0])
		dp = [ [0]*col for _ in range(row) ]
		dp[row-1][col-1] = 1
		for i in range(row-2, -1, -1):
			dp[i][col-1] = max(1, dp[i+1][col-1] - dungeon[i+1][col-1])
		for j in range(col-2, -1, -1):
			dp[row-1][j] = max(1, dp[row-1][j+1] - dungeon[row-1][j+1])

		for i in range(row-2, -1, -1):
			for j in range(col-2, -1, -1):
				left = max(1, dp[i][j+1] - dungeon[i][j+1])
				up = max(1, dp[i+1][j] - dungeon[i+1][j])
				dp[i][j] = min(left, up)

		print(np.array(dp))	
		return max(1, dp[0][0]-dungeon[0][0])


	def online_On(self, dungeon):
		"""
		:type dungeon: List[List[int]]
		:rtype: int
		"""
		"""
		min(dp[i+1], dp[i]) 这是正在更新dp
		dp[i+1]已经被更新过， 是当前位置的右边
		dp[i]还未被更新（正在）， 是当前位置的下边
		这个算法是竖着往左更新的
		"""
		m = len(dungeon)

		# Create boundary
		dp = [9999]*(m+1)
		dp[-2] = 1
		print(np.array(dp))
		for j in range(len(dungeon[-1])-1, -1, -1):
			print("==")
			for i in range(m-1, -1, -1):
				# We need at leat one point for survive
				print(np.array(dp))
				dp[i] = max(min(dp[i+1], dp[i]) - dungeon[i][j], 1)

		return dp[0]



dungeon = [ [-2,	-3,		3],
			[-5,	-10,	1],
			[10,	30,		-5] ]


sl = Solution()
print( sl.calculateMinimumHP( dungeon ) )
print( sl.online_On(dungeon) )
