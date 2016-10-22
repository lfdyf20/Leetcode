class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """ 
        res = []
        while matrix:
        	res += matrix.pop(0)
        	if matrix and matrix[0]:
        		for row in matrix:
        			res.append(row.pop())
        	if matrix:
        		res += matrix.pop()[::-1]
        	if matrix and matrix[0]:
        		for row in matrix[::-1]:
        			res.append(row.pop(0))
        return res


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix1 = [
 [ 1, 2 ],
 [ 4, 5 ],
]

matrix2 = [
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9,10,11,12 ],
 [13,14,15,16 ]
]

sl = Solution()
print( sl.spiralOrder( matrix2 ) )