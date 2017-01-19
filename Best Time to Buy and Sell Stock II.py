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
        	# print( prices[i] )
        	if prices[i] < sell:
        		profit += sell - buy
        		# print( "sell and buy with profit: " + repr(sell - buy) )
        		sell = buy = prices[i]
        	elif prices[i] > sell:
        		sell = prices[i]
        		# print( "keep" )
        profit += sell - buy
        return profit

    def mp(self, prices):
        if len(prices)<2:
            return 0
        low, high = prices[0], prices[0]
        profit = 0
        for price in prices[1:]:
            if price >= high:
                high = price
            else:
                profit += high - low
                high = low = price
        profit += high - low
        return profit

    def mySolution(self, prices):
        if len(prices) < 2:
            return 0
            
        maxProfit = 0
        buy = [-prices[0]]
        sell = [0]
        
        for p in prices[1:]:
            buy.append( max(buy[-1], sell[-1]-p) )
            sell.append( max(sell[-1], buy[-1]+p) )
        return max(sell)

    def online(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))









prices = [4,2,3,1,5,3,1,4,1,5,9,2,6]
sample = Solution()
print( sample.maxProfit( prices ) )
print(sample.mp(prices))