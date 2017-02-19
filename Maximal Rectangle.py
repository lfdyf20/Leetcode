class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
        	return 0
        n = len(matrix[0])
        height = [0] * (n+1)
        res = 0
        for row in matrix:
        	for i in range(n):
        		height[i] = height[i] + 1 if row[i] == '1' else 0
        	stack = []
        	for i in range(n+1):
        		if stack and height[i]<height[stack[-1]]:
        			while stack and height[i]<=height[stack[-1]]:
        				h = height[stack.pop()]
        				width = i if not stack else i-stack[-1]-1
        				res = max(res, h*width)
        		stack.append(i)
        return res
        



matrix = [
['1','1','1'],
['0','1','1'],
['0','0','1'],
]

sl = Solution()
print( sl.maximalRectangle( matrix ) )