import numpy as np
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """ 
        n = len(nums)
        rec = [ [0]*n for _ in range(n) ] 
        for i in range(n):
        	rec[i][i] = nums[i]
        	for j in range(i+1, n):
        		rec[i][j] = rec[i][j-1] + nums[j]
        print(np.array(rec))

        res = float('-inf')
        for i in range(n):
        	for j in range(i, n):
        		if j-i+1 < k:
        			rec[i][j] = 0
        		else:
        			rec[i][j] = rec[i][j]*1.0 / (j-i+1)
        			res = max(res, rec[i][j])
        print(np.array(rec))

        return res




    def mySolution(self, nums, k):
        n = len(nums)
        sumVal = sum(nums[:k])
        res = float('-inf')
        stack = [ (k-1, k, sumVal, sumVal*1.0/k) ]
        while stack:
        	index, kVal, sumVal, ave = stack.pop()
        	print(index, kVal, sumVal, ave)
        	res = max(res, ave)
        	if index + 1 < n:
        		tempSum = sumVal+nums[index+1]-nums[index-kVal+1]
        		stack.append( (index+1, kVal, tempSum, tempSum*1.0/kVal) )
        		if kVal-1 < index:
	        		tempSum = sumVal + nums[index-kVal]
	        		stack.append( (index, kVal+1, tempSum, tempSum*1.0/(kVal + 1)) ) 
        return res

nums = [9,7,3,5,6,2,0,8,1,9]
inde = [0,1,2,3,4,5,6,7,8,9]
k = 6

# nums = [1,12,-5,-6,50,3]
# inde = [0,1,  2, 3, 4,5]
# k = 4

sl = Solution()
print(nums)
print( sl.findMaxAverage( nums, k ) )
