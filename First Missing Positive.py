class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        add 0 is to avoid when all ele in nums is postive
        and consecutive [1,2,3,4] then we need one more room
        for the first postive 
        """ 
        nums.append(0)
        n = len(nums)
        for i in range( n ):
        	if nums[i] < 0 or nums[i]>n:
        		nums[i] = 0
        for i in range( n ):
        	nums[ nums[i]%n ] += n
        for i in range( n ):
        	if nums[i] < n:
        		return i
        return n


nums = [3,4,-1,1]
nums = [1]

sl = Solution()
print( sl.firstMissingPositive( nums ) )