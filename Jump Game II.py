class Solution:
    def jump(self, nums) -> int:
        size = len(nums)
        if size == 1:
            return 0
        steps = [i for i in range(size)]
        for i in range(size):
            coverage = i + nums[i] + 1
            if coverage >= size:
                return steps[i] + 1
            for coveredPos in range(i, coverage):
                steps[coveredPos] = min(steps[coveredPos], steps[i] + 1)
        else:
            return 0
        





nums = [2,3,1,1,4]
nums = [1,1,1,1,1,1]
nums = [4,1]
nums = [2,3,0,1,4]
# nums = [1]


sl = Solution()
print( sl.jump( nums ) )