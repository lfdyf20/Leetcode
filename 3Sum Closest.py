class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
        	j, k = i+1, len(nums)-1
        	while j<k:
        		sumVal = nums[i]+nums[j]+nums[k]
        		if sumVal == target:
        			return target
        		if abs(sumVal - target) <= abs(res - target):
        			res = sumVal
        		if sumVal < target:
        			j += 1
        		else:
        			k -= 1
        return res



nums, target = [1,2,1,-4], 1

sl = Solution()
print( sl.threeSumClosest( nums, target ) )



a =8
d = 3
m =2
b = 10*m + d
print(a**b == (a**d)*(a**(10*m) ))
