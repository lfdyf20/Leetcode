class Solution(object):
    def minCostII(self, cost):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(cost)
        if n == 0:
        	return 0
        if n == 1:
        	return min(cost[0])
        for i in range(1,n):
        	for j in range(len(cost[i])):
        		cost[i][j] += min(cost[i-1][:j]+cost[i-1][j+1:])
        return min(cost[-1])



costs = [[1,5,3],[2,9,4]]

sl = Solution()
print( sl.minCostII( costs ) )
print(costs)