class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        for num in nums:
        	if not stack or num > stack[-1][0] + 1:
        		stack.append( [num, 1] )
        		continue
        	elif num == stack[-1][0] + 1:
        		stack[-1][0] += 1
        		stack[-1][1] += 1
        	else:
        		for i in range(1, len(stack)):
        			if num == stack[~i][0] + 1:
        				stack[~i][0] += 1
        				stack[~i][1] += 1
        				break
        			elif num > stack[~i][0] + 1:
        				if stack[~i][1] < 3:
        					return False
        				stack.append( [num, 1] )
        				break
        		else:
        			stack.append( [num, 1] )
        	print(stack)
        return min(map(lambda x:x[1], stack)) >= 3

nums = [1,2,3,3,4,4,5,5]
# # nums = [1,2,3]
# nums = [1,2,3,4,5,6]

sl = Solution()
print( sl.isPossible( nums ) )