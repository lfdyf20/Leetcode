class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mix = (left + right) // 2
            if nums[mix] == target:
                return mix          
            elif nums[mix] < target:
                left = mix + 1
            elif nums[mix] > target:
                right = mix - 1
        return -1
            



nums = [-1,0,3,5,9,12]
target = 2


sl = Solution()
print( sl.search( nums, target ) )