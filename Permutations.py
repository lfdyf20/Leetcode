class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        return [ [n] + p
            for i, n in enumerate(nums)
            for p in self.permute( nums[:i] + nums[i+1:]) ] or [[]]

    def pm(self, nums):
    	def travel(nums, path, res):
    		if nums == []:
    			if path in res:
    				return
    			res.append( path )
    			return
    		for i, num in enumerate(nums):
    			travel(nums[:i]+nums[i+1:], path+[num], res)

    	res = []
    	travel(nums, [], res)
    	return res




nums = [1,2,3,4,5]
sl = Solution()
print( repr(sl.permute( nums )) )
print( sl.pm(nums) )
# print( nums[:0]+nums[1:] )
# print( repr(list(enumerate(nums))) )