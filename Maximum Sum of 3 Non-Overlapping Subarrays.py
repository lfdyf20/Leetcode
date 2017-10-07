class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        if len(nums) < 3*k:
            return []

        sumVals = [0] * ( len(nums)-k+1 )
        sumVals[0] = sum(nums[:k])
        for i in range(1, len(nums)-k+1):
            sumVals[i] = sumVals[i-1] + nums[i+k-1] - nums[i-1]

        dp_left = [ [0,0] for _ in range(len(sumVals)) ]
        dp_right = [ [0,0] for _ in range(len(sumVals)) ]

        dp_left_max = dp_right_max = float('-inf')

        for i in range(len(sumVals)):
            if sumVals[i] > dp_left_max:
                dp_left[i] = [ sumVals[i], i ]
                dp_left_max = sumVals[i]
            else:
                dp_left[i] = dp_left[i-1]

        for i in range(len(sumVals)-1, -1, -1):
            if sumVals[i] > dp_right_max:
                dp_right[i] = [ sumVals[i], i ]
                dp_right_max = sumVals[i]
            else:
                dp_right[i] = dp_right[i+1]

        res, maxVal = [], float('-inf')
        for i in range(k, len(sumVals)-k):
            if sumVals[i] + dp_left[i-k][0] + dp_right[i+k][0] > maxVal:
                res = [dp_left[i-k][1], i, dp_right[i+k][1]]
                maxVal = sumVals[i] + dp_left[i-k][0] + dp_right[i+k][0]
        return res

        	






nums, k = [1,2,1,2,6,7,5,1], 2

sl = Solution()
print( sl.maxSumOfThreeSubarrays(nums, k) )