class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
        	res ^= i
        return res

    def binary(self, nums):
    	l, r = 0, len(nums)-1
    	while l < r:
    		mid = (l+r)//2
    		if mid % 2 == 1:
    			mid -= 1
    		if nums[mid] != nums[mid+1]:
    			r = mid
    		else:
    			l = mid + 2
    	return nums[l]



nums = [3,7,7,11,11]

sl = Solution()
print( sl.singleNonDuplicate( nums ) )
print( sl.binary(nums) )