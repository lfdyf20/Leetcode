class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        r = ''.join(sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x]))
        return r.lstrip('0') or '0'









nums = [3, 30, 34, 5, 9]
sl = Solution()
print( sl.largestNumber(nums) )