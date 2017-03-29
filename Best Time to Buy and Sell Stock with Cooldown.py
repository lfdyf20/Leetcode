class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        buy = [0]*n
        sell = [0]*n
        cool = [0]*n
        buy[0] = -prices[0]
        for i in range(1, n):
        	buy[i] = max( buy[i-1], cool[i-1]-prices[i] )
        	cool[i] = sell[i-1]
        	sell[i] = max( sell[i-1], buy[i-1]+prices[i] )
        return max(cool[-1], sell[-1])


prices = [1,2,3,0,2]

sl = Solution()
print( sl.maxProfit( prices ) )