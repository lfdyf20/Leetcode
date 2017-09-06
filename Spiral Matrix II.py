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
	    print(result)
	    print(coord)
	    
	    count = 1
	    
	    while coord:
	        for x, y in coord.pop(0):
	            result[x][y] = count
	            count += 1
	        coord = zip(*coord)[::-1]

	    return result


	def mySolution(self, n):
		res = [ [0]*n for _ in range(n) ]
		i, j, di, dj = 0, 0, 0, 1
		for num in range(1, n**2+1):
			res[i][j] = num
			if res[(i+di)%n][(j+dj)%n]:
				di, dj = dj, -di
			i += di
			j += dj
		return res



n = 5
sl = Solution()
res = sl.generateMatrix(n)
print(np.matrix(res))
res = sl.mySolution(n)
print(np.matrix(res))



"""Mock Inetrview Solution

"""
import numpy as np
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
        	return []
        matrix = [ [0]*n for _ in range(n) ]
        print(len(matrix), len(matrix[0]))
        num = 1
        i, j = 0, 0
        while True:
        	while j < n and matrix[i][j] == 0:
        		matrix[i][j], num = num, num + 1
        		j += 1
        	i += 1
        	j -= 1
        	print(np.array(matrix))
        	if num > n**2:
        		break
        	while i < n and matrix[i][j] == 0:
        		matrix[i][j], num = num, num + 1
        		i += 1
        	j -= 1
        	i -= 1
        	print(np.array(matrix))
        	while j >= 0 and matrix[i][j] == 0:
        		matrix[i][j], num = num, num + 1
        		j -= 1
        	i -= 1
        	j += 1
        	print(np.array(matrix))
        	if num > n**2:
        		break
        	while i >= 0 and matrix[i][j] == 0:
        		matrix[i][j], num = num, num + 1
        		i -= 1
        	j += 1
        	i += 1
        	print(np.array(matrix))
        return matrix
