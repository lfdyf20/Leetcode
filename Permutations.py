class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        return [ [n] + p
            for i, n in enumerate(nums)
            for p in self.permute( nums[:i] + nums[i+1:]) ] or [[]]






nums = [1,2,3]
sl = Solution()
print( repr(sl.permute( nums )) )

# print( nums[:0]+nums[1:] )
# print( repr(list(enumerate(nums))) )