class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Min, Max = nums[0], nums[1]
        # pre = nums[1]
        # for num in nums[2:]:
        # 	if Min < num < Max:
        # 		print(Min, Max, num)
        # 		return True
        # 	Min = min(Min, pre)
        # 	Max = max(Max, num)
        # 	pre = num
        # else:
        # 	print(Min, Max, num)
        # 	return False

    def fp(self, nums):
    	if len(nums)<3:
    		return False
    	stack = [ [nums[0], nums[0]] ]
    	Min = nums[0]
    	for curr in nums[1:]:
    		if curr >= stack[0][1]:
    			stack = [ [Min, curr] ]
    		elif curr < Min:
    			stack.append( [curr, curr] )
    			Min = curr
    		elif curr == Min:
    			continue
    		else:
    			while stack and curr > stack[-1][0]:
    				if curr < stack[-1][1]:
    					return True
    				else:
    					stack.pop()
    			stack.append( [ Min, curr ] )
    	return False




nums = [3,1,4,1,5,9,2,6]
nums = [5,4,1,2,3]
# nums = [5,9,4,10]
# nums = [3,1,4,2]

sl = Solution()
print( sl.find132pattern( nums ) )
print(sl.fp( nums ))