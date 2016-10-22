class Solution(object):
    def productExceptSelf(self, nums):
        """
        Time limit exceeded
        
        :type nums: List[int]
        :rtype: List[int]
        """ 
        result = [1] * len(nums)
        for i in xrange(len(nums)):
        	newArray = [ nums[i]  ] * len(nums)
        	newArray[i] = 1
        	result = map(lambda x,y:x*y, newArray, result)
        return result




nums = [1,2,3,4]
sample = Solution()
print sample.productExceptSelf(nums)

