import random
from math import floor
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        low, high = 0, len(nums)-1
        print( nums[low], nums[high] )
        while high > low:
        	mid = floor(( low + high )/2)
        	if nums[mid] > nums[high]:
        		low = mid + 1
        	else:
        		high = mid if nums[high] != nums[mid] else high - 1
        return nums[low] 






nums = sorted([random.randint(0,100) for _ in range(100)])
b = random.randint(0,100)
nums = nums[b:] + nums[:b]
print(nums)

sl = Solution()
print( sl.findMin(nums) )