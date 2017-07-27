class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        nums.sort()
        print(nums)
        for i in range( len(nums)-2 ):
        	# print(nums[i])
        	l, r = i+1, len(nums)-1
        	while r > l:
        		if nums[i]+nums[l]+nums[r]<target:
        			res += r - l
        			l += 1
        		else:
        			r -= 1       		
        return res






nums, target = [-2, 0, 1, 3], 2
nums, target = [-1,1,-1,-1], -1

sl = Solution()
print( sl.threeSumSmaller( nums, target ) )