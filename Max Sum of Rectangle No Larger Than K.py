import itertools
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pass



    def maxSumSubmatrix0(self, matrix, k):
    	res = float('inf')
    	for i, j in itertools.product(range(len(matrix)-1), range(len(matrix[0])-1)):
    		for x, y in itertools.product(range(i+1,len(matrix)), range(j+1,len(matrix[0]))):
    			sumRec = self.compute(i,j,x,y,matrix)
    			print(sumRec)
    			if sumRec <= k and abs(k-sumRec) < abs(k-res):
    				res = sumRec
    	return res

    def compute(self, i, j, x, y, matrix):
    	res = 0
    	# print(matrix[j:y+1][i:x+1])
    	for row in matrix[i:x+1]:
    		res += sum(row[j:y+1])
    	return res




matrix = [
  [1,  0, 1],
  [0, -2, 3]
]

k = 2

sl = Solution()
print( sl.maxSumSubmatrix0( matrix, k ) )