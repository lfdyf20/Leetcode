class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)):
        	for j in range(len(triangle[i])):
        		upNode = self.findUpNode(i, j, triangle)
        		triangle[i][j] += min(upNode)
        		# print( upNode, triangle[i][j] )
       	return min(triangle[-1])


    def findUpNode(self, i, j, triangle):
    	if i==0 and j==0:
    		return [0,0]
    	if j==0:
    		return [float('inf'), triangle[i-1][0]]
    	if j==i:
    		return [triangle[i-1][-1], float('inf')]
    	return [triangle[i-1][j-1], triangle[i-1][j]]



        # if triangle == []:
        # 	return 0
        # if len(triangle)==1:
        # 	return triangle[0][0]
        # left = list( map(lambda x: x[:-1], triangle[1:]) )
        # right = list( map(lambda x: x[1:], triangle[1:]) )
        # return min(self.minimumTotal(left), self.minimumTotal(right))+triangle[0][0]

    def mt(self, triangle):
        if triangle == [[]]:
            return 0
        triangle.sort( key=len, reverse=True )
        for i, row in enumerate(triangle):
            for j in range(len(row)-1):
                triangle[i+1][j] += min( row[j], row[j+1] )
        print( triangle )
        return triangle[-1][0]
        


triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

triangle = [[]]

sl = Solution()
# print( sl.minimumTotal(triangle) )
print( sl.mt(triangle) )







