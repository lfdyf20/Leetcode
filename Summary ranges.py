class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if nums == result:
            return result
        start = end = nums[0]
        if len(nums) == 1:
            result.append(str(nums[0]))
        else:
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1] + 1:
                    end = nums[i]
                    if i == len(nums)-1:
                        result.append(str(start)+'->'+str(end))
                else:
                    if start == end:
                        result.append(str(nums[i-1]))
                    else:
                        result.append(str(start)+'->'+str(end))
                    start = end = nums[i]
                    if i == len(nums)-1:
                        result.append(str(nums[i]))
        return result





        

solution = Solution()
list = [0,3]
print list
print solution.summaryRanges(list)