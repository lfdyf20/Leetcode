from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        currCount = 1
        maxCount = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currCount += 1
            else:
                maxCount = max( maxCount, currCount )
                currCount = 1
        
        return max( maxCount, currCount )

        



nums = [1,3,5,4,7, 8, 9,9, 11, 12]


sl = Solution()
print( sl.findLengthOfLCIS( nums ) )