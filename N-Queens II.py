class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        self.res = 0

        def valid(nums, n):
        	if any( (nums[i]==nums[n] or (abs(nums[n]-nums[i]) == n-i)) for i in range(n)):
        		return False
        	return True

        def travel(nums, index):
        	if index == len(nums):
        		self.res += 1
        		return
        	for i in range( len(nums) ):
        		nums[ index ] = i
        		if valid(nums, index):
        			travel(nums, index+1)

        travel( [-1]*n, 0 )
        return self.res

        


n = 8
sl = Solution()
print( sl.totalNQueens(n) )