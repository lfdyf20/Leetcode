class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        for i in range( len(nums) ):
        	if nums[i]==0:
        		nums.pop(i)
        		nums.insert(0,0)
        for i in range( len(nums)-1, -1, -1):
        	if nums[i]==2:
        		nums.pop(i)
        		nums.append(2)





nums = [0,2,1,2,1,0,2]
sl = Solution()
sl.sortColors(nums)
print(nums)