class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # if ( len(nums)<2 ):
        # 	return False
        # nums.sort()
        # i = 0
        # while( i < (len(nums)-1) ):
        # 	if nums[i] == nums[i+1]:
        # 		i = i + 1 
        # 		return True
        # 	else:
        # 		i = i + 1
        # return False



        

i = 0
sample = Solution()
nums = [3,1,1]
print sample.containsDuplicate( nums )

set(nums)
print len( set(nums) )

