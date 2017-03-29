class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        n = len(nums)
        if n<=2:
        	return n
        curr = nums[-1]
        count = 1
        dupLen = 0
        for i in range( -2, -n-1, -1 ):
        	if nums[i]==curr:
        		count += 1
        		if count > 2:
        			dupLen += 1
        			nums.pop(i)
        			nums.append(curr)
        	else:
        		curr = nums[i]
        		count = 1
        return n - dupLen

    def mySolution( self, nums ):
        n = len(nums)
        if n <= 2:
            return n
        curr = nums[~0]
        count = 1
        for i in range(1, len(nums)):
            if nums[~i] == curr:
                count += 1
                if count > 2:
                    n -= 1
                    nums.append( nums.pop(~i) )
            else:
                curr = nums[~i]
                count = 1
        return n

    def online(self, nums):
        left = 0
        for num in nums:
            if left < 2 or num > nums[ left-2 ]:
                nums[left] = num
                left += 1
        return left



nums = [1,1,1]
sl = Solution()
print( sl.removeDuplicates(nums) )
print(nums)

nums = [1,1,1]
print( sl.mySolution(nums) )
print(nums)