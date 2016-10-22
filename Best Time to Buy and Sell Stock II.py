class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        if len(prices)<2:
        	return 0
        profit = 0
        buy = sell = prices[0]
        for i in range( 1, len(prices) ):
        	print( prices[i] )
        	if prices[i] < sell:
        		profit += sell - buy
        		print( "sell and buy with profit: " + repr(sell - buy) )
        		sell = buy = prices[i]
        	elif prices[i] > sell:
        		sell = prices[i]
        		print( "keep" )
        profit += sell - buy
        return profit









prices = [4,2,3,1,5]
sample = Solution()
print( sample.maxProfit( prices ) )