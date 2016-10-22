class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
        	return True
        
        curr = 0
        
        while curr < len(nums): 
        	if curr < 0:
        		return False
        	if curr >= len(nums)-1:
        		return True
        	if nums[curr] == 0:
        		currMax = curr
        		while nums[curr] + curr <= currMax:
        			curr -= 1
        			if curr < 0:
        				return False
        	curr += nums[curr]
        return True


nums = [3,8,1,0,0,0,0,2]
nums = [2,2,0,1] 
sl = Solution()
print( sl.canJump( nums ) )