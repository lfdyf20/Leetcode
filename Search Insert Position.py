class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        for i in range( len(nums) ):
        	if nums[i]==target:
        		return i
        	if nums[i] > target:
        		return i
        return len(nums)

    def mySolution(self, nums, target):
        l, r = 0, len(nums)
        if target > nums[-1]:
            return r
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l




nums = [1,3]
target = 1
sl = Solution()
print( sl.searchInsert(nums, target) )
print( sl.mySolution(nums, target) )