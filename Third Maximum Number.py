class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted({i for i in nums})
        return nums[-3] if len(nums) >= 3 else max(nums)

    def thirdMax2(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]


nums = [1, 2]

sl = Solution()
print( sl.thirdMax( nums ) )