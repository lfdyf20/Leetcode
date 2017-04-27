class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        record, stack = {}, []
        for num in nums:
        	while stack and stack[-1]<num:
        		record[ stack.pop() ] = num
        	stack.append(num)
        res = []
        for num in findNums:
        	if num in record:
        		res.append( record[num] )
        	else:
        		res.append(-1)
        return res


findNums, nums = [4,1,2], [1,3,4,2] 

sl = Solution()
print( sl.nextGreaterElement( findNums, nums ) )