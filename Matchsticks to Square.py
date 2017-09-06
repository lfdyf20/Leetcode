class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(pos, target):
        	for i in range(4):
        		if pos == len(nums):
        			return True
        		if target[i] >= nums[pos]:
        			target[i] -= nums[pos]
        			if dfs(pos+1, target):
        				return True
        			target[i] += nums[pos]
        	return False

        if len(nums) < 4:
        	return False
        sumVal = sum(nums)
        if sumVal % 4 > 0:
        	return False
        nums.sort(reverse=True)
       	target = [ sumVal // 4 ] * 4
       	return dfs(0, target)
        



nums = [1,1,2,2,2]

sl = Solution()
print( sl.makesquare( nums ) )