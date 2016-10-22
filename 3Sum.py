import time
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range( len(nums)-2 ):
        	if i > 0 and nums[i] == nums[i-1]:
        		continue
        	l, r = i+1, len(nums)-1
        	while l < r:
        		# print([nums[i], nums[l], nums[r]])
        		s = nums[i] + nums[l] + nums[r]
        		# print(s)
        		if s < 0:
        			l += 1
        		elif s > 0:
        			r -= 1
        		else:
        			# print("bingo")
        			res.append( [nums[i], nums[l], nums[r]] )
        			while l < r and nums[l] == nums[l+1]:
        				l += 1
        			while l < r and nums[r] == nums[r-1]:
        				r -= 1
        			l += 1
        			r -= 1
        return res
        # time limit exceeded
        # if len(nums)<3:
        # 	return []
        # nums.sort()
        # res = []
        # for i in range( len(nums)-2 ):
        # 	for j in range(i+1, len(nums)-1):
        # 		z = 0 - nums[i] - nums[j]
        # 		if z in nums[j+1:]:
        # 			path = sorted([nums[i], nums[j], z])
        # 			if path not in res:
        # 				res.append( path )
        # return res






nums = [-1, 0, 1, 2, -1, -4]
# nums = [12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1]

sl = Solution()
stt = time.time()
print( sl.threeSum( nums ) )
print(time.time() - stt)