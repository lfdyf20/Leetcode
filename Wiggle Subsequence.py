class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 

        up = down = 0
        for i in range(len(nums)):
        	if i==0:
        		up = down = 1
        		continue
        	if nums[i]>nums[i-1]:
        		up, down = down+1, down
        	elif nums[i]<nums[i-1]:
        		up, down = up, up+1

        	else:
        		continue
        return max(up, down)


sl = Solution()
nums = [1,7,4,9,2,5]
nums = []
print( sl.wiggleMaxLength(nums) )