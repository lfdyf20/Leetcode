class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(map(int, str(n)))
        for i in range(len(nums)):
        	if i == 0:
        		continue
        	if nums[~i] < nums[~i+1]:
        		for j in range(i):
        			if nums[~j] > nums[~i]:
        				nums[~j], nums[~i] = nums[~i], nums[~j]
        				break
        		break
        else:
        	return -1
        nums = nums[:~i+1] + sorted(nums[~i+1:])
        return int(''.join(map(str, nums)))





n = 12443322

sl = Solution()
print( sl.nextGreaterElement( n ) )