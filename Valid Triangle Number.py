class Solution(object):

	#SPEED: 
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums.sort()
        for i in range(2, len(nums)):
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    ans += end - start
                    end -= 1
                else:
                    start += 1
        return ans



nums = [2,2,3,4]

sl = Solution()
print( sl.triangleNumber( nums ) )