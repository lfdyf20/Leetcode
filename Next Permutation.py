class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n+1):
        	# print(nums[-i])
        	if i == 1:
        		maxVal = nums[-i]
        	if nums[-i] < maxVal:
        		print("nums[-i]:",nums[-i], " < ", "maxVal: ",maxVal)
        		for j in range(1, i):
        			if nums[-j] > nums[-i]:
        				print("nums[-j]: ", nums[-j], " > ", "nums[-i]: ", nums[-i])
        				nums[-j], nums[-i] = nums[-i], nums[-j]
        				nums[-i+1:] = sorted(nums[-i+1:])
        				return
        	else:
        		maxVal = nums[-i]
        nums.sort()
    
    def mySolution(self, nums):
        maxVal = nums[~0]
        for i in range(1, len(nums)):
            if nums[~i] < maxVal:
                for j in range(len(nums)):
                    if nums[~i] < nums[~j]:
                        print(nums[~i], nums[~j])
                        nums[~i], nums[~j] = nums[~j], nums[~i]
                        nums[~i+1:] = sorted( nums[~i+1:] )
                        return
            else:
                maxVal = nums[~i]
        nums.sort()







nums = [1,3,2]
nums = [2,1,3]

sl = Solution()
# sl.nextPermutation( nums )
sl.mySolution(nums)
print(nums)
