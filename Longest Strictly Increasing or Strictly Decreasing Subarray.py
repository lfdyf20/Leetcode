class Solution:
    def longestMonotonicSubarray(self, nums) -> int:
        prev = 1
        increase = True
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if i == 1:
                    increase = True

                if increase:
                    curr += 1
                else:
                    increase = True
                    prev = max(prev, curr)
                    curr = 2
            elif nums[i] < nums[i-1]:
                if i == 1:
                    increase = False
                    
                if not increase:
                    curr += 1
                else:
                    increase = False
                    prev = max(prev, curr)
                    curr = 2
            else:
                prev = max(prev, curr)
                curr = 1
        return max(prev, curr)



nums = [1,5,2,7]


sl = Solution()
print( sl.longestMonotonicSubarray( nums ) )