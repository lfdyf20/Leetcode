from math import factorial
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<2:
        	return 0
        diff = [j-i for i, j in zip( A[:-1], A[1:] ) ]
        print(diff)
        res = 0
        count = 1
        pre = diff[0]
        for i in diff[1:]:
        	if i == pre:
        		count += 1
        	else:
        		pre = i
        		if count > 1:
        			count += 1
        			# print("count:", count)
        			res += ((count-2) * (count-1)//2)
        		count = 1
        if count > 1:
        	count += 1
        	res += ((count-2) * (count-1)//2)
        return res




A = [1,2,3,5,7,8,4,7,10,13,5]
# A = [1,2,3,4]
# A = [1,2,3,8,9,10]
A = [1]

sl = Solution()
print( sl.numberOfArithmeticSlices( A ) )