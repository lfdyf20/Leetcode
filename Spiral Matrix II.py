import numpy as np
class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		ma = [[0 for i in range(n)] for i in range(n)]
		count = 0
		i = j = 0
		num = 1
		while True and count<n+2:
			print("right")
			while j<n-count:# and ma[i][j]==0:
				ma[i][j] = num
				j += 1
				num += 1
			if num == n*n:
				return ma
			i, j= i+1, j-1
			
			print("down")
			while i<n-count:# and ma[i][j] == 0:
				ma[i][j] = num
				i += 1
				num += 1
			i, j= i-1, j-1

			print("left")
			while j>=count:# and ma[i][j] == 0:
				ma[i][j] = num
				j -= 1
				num += 1
			if num == n*n:
				return ma
			i, j= i-1, j+1

			print("up")
			while i>count:# and ma[i][j] == 0:
				ma[i][j] = num
				i -= 1
				num += 1
			i, j= i+1, j+1

			count += 1
		return ma

	def generateMatrix2(self, n):  
	    result = [[0 for i in range(n)] for j in range(n)]
	    coord = [[(i,j) for j in range(n)] for i in range(n)]
	    
	    count = 1
	    
	    while coord:
	        for x, y in coord.pop(0):
	            result[x][y] = count
	            count += 1
	        coord = zip(*coord)[::-1]

	    return result


n = 5
sl = Solution()
res = sl.generateMatrix(n)
print(np.matrix(res))
