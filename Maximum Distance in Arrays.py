class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        curMin, curMax, res = float('inf'), float('-inf'), 0
        for a in arrays:
        	res = max(res, a[-1]-curMin, curMax-a[0])
        	curMax = max(curMax, a[-1])
        	curMin = min(curMin, a[0])
        return res


arrays = [[1,2,3],
 [4,5],
 [1,2,3]]

sl = Solution()
print( sl.maxDistance( arrays ) )