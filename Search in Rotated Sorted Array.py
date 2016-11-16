class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
        	return 0 if nums[0] == target else -1
        lv, rv = nums[0], nums[-1]
       	l, r = 0, len(nums)-1
        if lv < rv:
        	mid = 0
        else:
	        mid = (l+r)//2
	        while r >= l:
	        	# print(nums[l], nums[mid], nums[r])
	        	if nums[mid] >= lv:
	        		l = mid + 1
	        	if nums[mid] <= rv:
	        		r = mid - 1
	        	mid = (l+r)//2
        l, r = r, l
        # print(nums[l], nums[r])

        if target > nums[0]:
        	l, r = 0, l
        elif target < nums[-1]:
        	l, r = r, len(nums)-1
        elif target == nums[0]:
        	return 0
        elif target == nums[-1]:
        	return len(nums)-1
        else:
        	return -1
        	

        # print(nums[l], nums[r])
        mid = (l+r)//2
        while r > l:
        	if nums[mid] < target:
        		l = mid + 1
        	elif nums[mid] > target:
        		r = mid - 1
        	else:
        		return mid
        	mid = (l+r)//2
        # print(nums[l], nums[r])
        if nums[l] != target:
        	return -1
        else:
        	return l
        





nums, target = [3, 4, 5, 6, 7, 0, 1, 2], 0
nums = [1,2]


sl = Solution()
print( sl.search( nums, target ) )