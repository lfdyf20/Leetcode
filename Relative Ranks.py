class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rec = sorted([(num, i) for i,num in enumerate(nums)],reverse=True)
        for i in range(len(rec)):
        	index = rec[i][1]
        	if i == 0:
        		nums[index] = "Gold Medal"
        	elif i == 1:
        		nums[index] = "Silver Medal"
        	elif i == 2:
        		nums[index] = "Bronze Medal"
        	else:
        		nums[index] = str(i+1)
        return nums
     


nums = [4, 5, 3, 2, 1]

sl = Solution()
print( sl.findRelativeRanks( nums ) )