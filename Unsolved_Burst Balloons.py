class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        totalCoins = 0
        currentMinPos = self.findMin( nums )
        while len(nums)>3:
        	pos = self.findMin( nums[1:-1] )
        	pos += 1
        	print( 'min number is:' + repr(nums[pos]) )
        	totalCoins += self.sumCoins( pos, nums )
        	nums.pop( pos )
        if len(nums) == 3:
        	print( 'min number is:' + repr(nums[1]) )
        	totalCoins += self.sumCoins( 1, nums )
        	nums.pop( 1 )
        while len(nums) < 3 and nums != []:
        	pos = self.findMin( nums )
        	print( 'min number is:' + repr(nums[pos]) )
        	totalCoins += self.sumCoins( pos, nums )
        	nums.pop( pos )
        return totalCoins


    def findMin( self, nums ):
    	print("findMin--> nums:"+repr(nums))
    	minPos = 0
    	minVal = 101
    	for i in range( len(nums) ):
    		if nums[i]< minVal:
    			minPos, minVal = i, nums[i]
    		else:
    			pass
    	return minPos

    def sumCoins(self, pos, nums):
    	coins = 0
    	if  pos>0 and pos< len(nums)-1:
    		coins = nums[pos-1] * nums[pos] * nums[pos+1]
    	elif pos == 0 and len(nums) == 2:
    		coins = 1 * nums[pos] * nums[pos+1]
    	elif pos == 0 and len(nums) == 1:
    		coins = 1 * nums[pos] * 1
    	elif pos == len(nums)-1:
    		coins = nums[pos-1] * nums[pos] * 1
    	else:
    		print('something wrong: pos:'+repr(pos))
    	return coins


    def maxCoins2(self, iNums):
	    nums = [1] + [i for i in iNums if i > 0] + [1]
	    n = len(nums)
	    dp = [[0]*n for _ in range(n)]
	    print( "dp="+repr(dp) )

	    for k in range(2, n):
	        for left in range(0, n - k):
	            right = left + k
	            for i in range(left + 1,right):
	                dp[left][right] = max(dp[left][right],
	                       nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
	                print( "dp="+repr(dp) )
	    return dp[0][n - 1]






nums = [9,76,64,21,97,60]
sample = Solution()
print( sample.maxCoins2( nums ) )
# print( sample.findMin([33]) )
# print(len(nums))
# print( nums[1:-1] )
