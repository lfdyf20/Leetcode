class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
        	return 0
        length, count = [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):
        	for j in range(i):
        		if nums[j] < nums[i]:
        			if length[j] + 1 == length[i]:
        				count[i] += count[j]
        			elif length[j] + 1 > length[i]:
        				count[i] = count[j]
        				length[i] = length[j] + 1
       	return sum((y for x,y in zip(length, count) if x==max(length)))

        	


        




nums = [1,3,5,4,7]
# nums = [2,2,2,2,2]
# nums = [1,2,8,7,9,10,4,3,11]
nums = []
# nums = [1]
# nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [1,2,3,3,3,2,1]
nums = [1,2,3,3,3]
nums = [1,2,4,3,5,4,7,2]


sl = Solution()
print( sl.findNumberOfLIS( nums ) )