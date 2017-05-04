class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        numbers = [ nums[i][j] for i in range(len(nums)) \
        					for j in range(len(nums[i])) ][::-1]
        if len(numbers) != r*c:
        	return nums
        res =[]
        for i in range(r):
        	row = []
        	for j in range(c):
        		row.append( numbers.pop() )
        	res.append(row)
        return res



nums = [[1,2],
 		[3,4]]
r, c = 1, 4

sl = Solution()
print( sl.matrixReshape( nums, r, c ) )